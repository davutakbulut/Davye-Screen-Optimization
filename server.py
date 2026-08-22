import http.server
import socketserver
import json
import subprocess
import os
import re

PORT = 8888
DIRECTORY = "/Users/davutakbulut/Desktop/siparis-sayfasi"

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_POST(self):
        if self.path == '/api/save-content':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            try:
                payload = json.loads(post_data.decode('utf-8'))
                old_val = payload.get('oldValue', '')
                new_val = payload.get('newValue', '')
                full_html = payload.get('fullHtml', '')

                if full_html:
                    with open(os.path.join(DIRECTORY, 'index.html'), 'w', encoding='utf-8') as f:
                        f.write(full_html)
                elif old_val and new_val:
                    with open(os.path.join(DIRECTORY, 'index.html'), 'r', encoding='utf-8') as f:
                        content = f.read()
                    if old_val in content:
                        content = content.replace(old_val, new_val, 1)
                        with open(os.path.join(DIRECTORY, 'index.html'), 'w', encoding='utf-8') as f:
                            f.write(content)

                # Async Git Commit & Push
                subprocess.Popen(['git', 'add', 'index.html'], cwd=DIRECTORY).wait()
                subprocess.Popen(['git', 'commit', '-m', f'edit: update field {old_val[:20]} -> {new_val[:20]}'], cwd=DIRECTORY).wait()
                subprocess.Popen(['git', 'push', 'origin', 'main'], cwd=DIRECTORY)

                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(json.dumps({'success': True}).encode('utf-8'))
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(json.dumps({'success': False, 'error': str(e)}).encode('utf-8'))
        else:
            self.send_error(404, "Endpoint not found")

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("127.0.0.1", PORT), CustomHandler) as httpd:
    print(f"Serving API and static files at port {PORT}")
    httpd.serve_forever()
