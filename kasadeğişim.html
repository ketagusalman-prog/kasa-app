<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Yapay Zeka Destekli Adaletli Rotasyon</title>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;800&display=swap" rel="stylesheet">
    <style>
        :root { --bg: #0b0f1a; --card: #161e31; --accent: #3b82f6; --text: #ffffff; --green: #10b981; --orange: #f59e0b; }
        body { font-family: 'Plus Jakarta Sans', sans-serif; background: var(--bg); color: var(--text); padding: 15px; margin: 0; }
        .header { text-align: center; border-bottom: 2px solid var(--accent); padding-bottom: 15px; margin-bottom: 20px; }
        .match-card { 
            display: flex; align-items: center; justify-content: space-between; 
            background: rgba(255,255,255,0.03); padding: 15px; border-radius: 12px; margin-bottom: 10px;
            border-left: 4px solid var(--accent); position: relative;
        }
        .balance-badge { 
            position: absolute; top: 0; right: 20px; background: var(--green); 
            color: #000; font-size: 8px; font-weight: 800; padding: 2px 8px; border-radius: 0 0 8px 8px;
        }
        .person { flex: 1; display: flex; flex-direction: column; }
        .person span { font-size: 9px; color: #94a3b8; font-weight: 800; text-transform: uppercase; }
        .person strong { font-size: 14px; margin-top: 2px; }
        .arrow { flex: 0 0 40px; text-align: center; font-size: 18px; color: var(--accent); }
        .kasa-tag { background: #334155; color: #fff; padding: 2px 6px; border-radius: 4px; font-size: 10px; margin-right: 4px; }
        h2 { font-size: 11px; text-transform: uppercase; color: var(--orange); margin: 25px 0 10px 0; letter-spacing: 1px; border-bottom: 1px solid rgba(255,165,0,0.2); padding-bottom: 5px;}
        .history-tag { font-size: 8px; color: #64748b; margin-top: 2px; font-style: italic; }
    </style>
</head>
<body>

<div class="header">
    <h1 style="font-size: 18px; margin: 0;">⚖️ GEÇMİŞE DUYARLI ADALET SİSTEMİ</h1>
    <p style="font-size: 10px; opacity: 0.7; margin-top: 5px;">Kişinin gün içindeki tüm kasaları hesaplanır.</p>
</div>

<div id="rotasyonListesi"></div>

<script type="module">
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-app.js";
import { getFirestore, doc, onSnapshot } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-firestore.js";

const firebaseConfig = { apiKey: "AIzaSy...", authDomain: "ukasa1.firebaseapp.com", projectId: "ukasa1" };
const app = initializeApp(firebaseConfig);
const db = getFirestore(app);

const yogunlukSirasi = [12, 11, 10, 8, 7, 9, 6, 4, 5, 3, 2, 1];

const molaAkisi = [
    { donen: "cay4",   giden: "yemek3", baslik: "ÇAY 4 DÖNÜŞ ➔ YEMEK 3 ÇIKIŞ" },
    { donen: "yemek3", giden: "yemek4", baslik: "YEMEK 3 DÖNÜŞ ➔ YEMEK 4 ÇIKIŞ" },
    { donen: "yemek4", giden: "son1",   baslik: "YEMEK 4 DÖNÜŞ ➔ SON 1 ÇIKIŞ" },
    { donen: "son1",   giden: "son2",   baslik: "SON 1 DÖNÜŞ ➔ SON 2 ÇIKIŞ" },
    { donen: "son2",   giden: "son3",   baslik: "SON 2 DÖNÜŞ ➔ SON 3 ÇIKIŞ" },
    { donen: "son3",   giden: "son4",   baslik: "SON 3 DÖNÜŞ ➔ SON 4 ÇIKIŞ" },
    { donen: "son4",   giden: "cay4",   baslik: "SON 4 DÖNÜŞ ➔ ÇAY 4 (FİNAL)" }
];

onSnapshot(doc(db, "kasa", "liste"), (kasaSnap) => {
    onSnapshot(doc(db, "kasa", "mola"), (molaSnap) => {
        const kasalar = kasaSnap.exists() ? (kasaSnap.data().data || {}) : {};
        const molalar = molaSnap.exists() ? (molaSnap.data().data || {}) : {};
        const listeDiv = document.getElementById("rotasyonListesi");
        listeDiv.innerHTML = "";

        // HAFIZA SİSTEMİ (GEÇMİŞİ TUTAR)
        let isimKasaGecmisi = {}; 
        
        // İlk kasa bilgisini al
        Object.keys(kasalar).forEach(k => {
            const isim = kasalar[k]?.isim?.trim();
            if(isim) {
                if(!isimKasaGecmisi[isim]) isimKasaGecmisi[isim] = [];
                isimKasaGecmisi[isim].push(parseInt(k.replace("kasa", "")));
            }
        });

        molaAkisi.forEach(akis => {
            const donenIsimleri = (molalar[akis.donen]?.kisiler || []).filter(n => n && n.trim() !== "").map(n => n.trim());
            const gidenIsimleri = (molalar[akis.giden]?.kisiler || []).filter(n => n && n.trim() !== "").map(n => n.trim());

            if (donenIsimleri.length > 0 && gidenIsimleri.length > 0) {
                listeDiv.innerHTML += `<h2>${akis.baslik}</h2>`;

                // 1. DÖNENLER: Yoğunluk Puanı Hesapla (Tüm geçmiş kasaların ortalama ağırlığı)
                let donenlerHavuzu = donenIsimleri.map(isim => {
                    let gecmis = isimKasaGecmisi[isim] || [];
                    // En yoğun kasayı baz al (Daha adaletli olur)
                    let enYogunKasaIndexi = Math.min(...gecmis.map(k => {
                        let idx = yogunlukSirasi.indexOf(k);
                        return idx === -1 ? 99 : idx;
                    }));

                    return { 
                        isim, 
                        sonKasa: gecmis[gecmis.length - 1] || "?", 
                        gecmisText: gecmis.join(", "),
                        siraPuanı: enYogunKasaIndexi === Infinity ? -1 : enYogunKasaIndexi 
                    };
                }).sort((a, b) => a.siraPuanı - b.siraPuanı); 

                // 2. GİDECEKLER: Boşalanlar içinde sakin olanı başa al
                let gideceklerHavuzu = [];
                gidenIsimleri.forEach(gidenIsim => {
                    let gecmis = isimKasaGecmisi[gidenIsim] || [];
                    let kNo = gecmis[gecmis.length - 1];
                    if(kNo) {
                        let siraIndex = yogunlukSirasi.indexOf(kNo);
                        gideceklerHavuzu.push({ isim: gidenIsim, kasaNo: kNo, sira: siraIndex });
                    }
                });
                gideceklerHavuzu.sort((a, b) => b.sira - a.sira);

                // 3. EŞLEŞTİRME VE GEÇMİŞİ GÜNCELLEME
                donenlerHavuzu.forEach((donen, i) => {
                    const gidecek = gideceklerHavuzu[i];
                    if(gidecek) {
                        // Yeni kasayı geçmişe ekle, eskisini unutma!
                        if(!isimKasaGecmisi[donen.isim]) isimKasaGecmisi[donen.isim] = [];
                        isimKasaGecmisi[donen.isim].push(parseInt(gidecek.kasaNo));

                        listeDiv.innerHTML += `
                            <div class="match-card">
                                <div class="balance-badge">GEÇMİŞE DUYARLI ADALET</div>
                                <div class="person">
                                    <span><span class="kasa-tag">KASA ${gidecek.kasaNo}</span> ÇIKIŞ</span>
                                    <strong>${gidecek.isim}</strong>
                                </div>
                                <div class="arrow">➜</div>
                                <div class="person" style="text-align: right;">
                                    <span>YENİ GEÇEN</span>
                                    <strong>${donen.isim}</strong>
                                    <div class="history-tag">Geçmiş: ${donen.gecmisText} ➔ Yeni: ${gidecek.kasaNo}</div>
                                </div>
                            </div>`;
                    }
                });
            }
        });
    });
});
</script>
</body>
</html>
