import { Component } from '@angular/core';

export interface Urun {
  ad: string;
  icerik: string;
  tsfFiyat: number;
  koliFiyat: number;
}

export interface UrunGrubu {
  baslik: string;
  urunler: Urun[];
}

const fort: Urun = { ad: 'Maxicaine Ds Fort', icerik: 'Artikain HCl %4, Epinefrin 1/100.000', tsfFiyat: 425, koliFiyat: 25505 };
const ds: Urun = { ad: 'Maxicaine Ds', icerik: 'Artikain HCl %4, Epinefrin 1/200.000', tsfFiyat: 425, koliFiyat: 25505 };
const jetokain: Urun = { ad: 'Jetokain', icerik: 'Lidocain HCl %10, Epinefrin 10/500', tsfFiyat: 425, koliFiyat: 25505 };

@Component({
  selector: 'app-katalog',
  standalone: true,
  templateUrl: './katalog.component.html',
  styleUrl: './katalog.component.css',
})
export class KatalogComponent {
  tarih = '28.10.2026';
  kategori = 'Lokal Anezteziler';
  ucretsizKargoLimiti = 6500;

  // Veriler Katalog.pdf'ten birebir alındı
  gruplar: UrunGrubu[] = [
    { baslik: 'Artikain / Ampul', urunler: [fort, ds, fort, ds] },
    { baslik: 'Artikain / Karpül', urunler: [fort, ds] },
    { baslik: 'Lidokain / Ampul', urunler: [jetokain, ds] },
    { baslik: 'Lidokain / Spreyler', urunler: [fort, ds, fort, ds] },
  ];

  fiyat(deger: number): string {
    return deger.toLocaleString('tr-TR') + '₺';
  }
}
