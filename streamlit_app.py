import streamlit as st
from PIL import Image
import datetime



from streamlit_option_menu import option_menu

# st.title("Streamlit Option Menu")

# 2. as horizontal menu  (identation'lara dikkat edin)

selected = option_menu(
        menu_title=None, #required
        options=["Anasayfa", "Proje", "Analiz", "Öneriler"], #required
        icons= ["house", "book", "envelope", "fork"],#optional (isimlerin yanına ikon eklemek için) ,
        menu_icon="cast", # optional
        default_index=0, #optional
        orientation = "horizontal",
        # önce alttaki styles bolumu olmadan sayfayı run edin
        #sonra styles kullanarak farkı görun
        styles={
                "container": {"padding": "0!important", "background-color": "#fafafa"},
                "icon": {"color": "#00ffgg", "font-size": "18px"},
                "nav-link": {
                    "font-size": "18px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "#eee",
                    "font-family": "Arial"
                },
                "nav-link-selected": {"background-color": "#000080"},
            },
)

# yukardaki selected kısmının seçeneğe bağlı çalışması için alttaki if cümleleri yazılır
#ilgili menu içinde yapılacaklar alttaki if cümlesinin altında st.title altında yapılabliir
if selected == "Anasayfa": 
    st.title(f"Mekansal Birey Kalma Süresi Analizi ")
    img2=Image.open("techpro.png")
    st.image(img2, width=300)
    st.markdown("""  Proje Kamera ile alınan görüntülerden kişilerin
                 bir alan içinde ne kadar kaldığını bulan ve sonrasında
                 burdaki verilerle analiz yapan bir sistemdir.""")
    #today=st.date_input(datetime.datetime.now())
    st.header("Yapılan çalışmadan bir görüntü")

    img1=Image.open("video.png")  
    st.image(img1, width=600, caption="süre ve kişiler")
    
    st.header("Mekansal Birey Kalma Süresi Analizi Bir Market Reyonu için yapılırsa")
    st.markdown("""
    ## Akıllı Mağaza Sistemleri
    Müşteri davranışlarını izleyerek ve analiz ederek mağaza içi operasyonları optimize etmenizi sağlayan teknolojilerdir. Bu tür sistemler, müşteri deneyimini iyileştirmek, personel verimliliğini artırmak ve satışları optimize etmek için birçok avantaj sunar. Akıllı mağaza sistemleri için önerilerim şunlar:

    1. Müşteri Takip ve Analiz Sistemleri:

    **Kamera Tabanlı İzleme:** Yüksek çözünürlüklü kameralar ve yapay zeka algoritmaları kullanarak mağaza içinde müşterilerin hareketlerini takip edebilirsiniz. Bu sistemler, hangi reyonların daha fazla ilgi gördüğünü, nerelerde yığılma yaşandığını ve müşterilerin mağaza içinde izledikleri yolları analiz etmenize olanak tanır.

    **Isı Haritaları (Heatmaps):** Kamera verileriyle oluşturulan ısı haritaları, mağazada en çok ziyaret edilen bölgeleri ve ilgi gören reyonları belirlemenizi sağlar. Bu veriler, ürün yerleşimini optimize etmek ve müşteri akışını iyileştirmek için kullanılabilir.

    **RFID Takip Sistemleri:** Ürünlere yerleştirilen RFID etiketleri ile ürünlerin hareketleri izlenebilir ve müşterilerin hangi ürünlere ilgi gösterdiği, hangi ürünlerin daha fazla incelendiği veya satın alındığı analiz edilebilir.
    """)
    st.header("Mobil Uygulamalar")

    img3=Image.open("mobil.png")
    st.image(img3, width=600)
    st.markdown("""
    2. Kişiselleştirilmiş Müşteri Deneyimi:

    **Dijital Kiosklar:** Müşterilere mağaza içi yönlendirme, ürün bilgileri, kampanyalar ve özel teklifler sunan dijital kiosklar yerleştirilebilir. Bu kiosklar, müşterilerin ilgi alanlarına göre kişiselleştirilmiş öneriler sunabilir.

    **Mobil Uygulamalar ve Beacons:** Mobil uygulamalar aracılığıyla müşterilere, mağazada gezindikleri sırada özel indirimler veya ürün önerileri sunabilirsiniz. Beacon teknolojisi kullanarak, müşterilerin konumuna göre kişiselleştirilmiş bildirimler gönderebilirsiniz.
    """)
    st.header("Akıllı Sepetler")
    img4=Image.open("sepet.png")
    st.image(img4, width=600)
    st.markdown("""
    3. Self-Checkout Sistemleri:

    **Akıllı Sepetler:** Müşterilerin alışveriş yaparken sepetlerine ekledikleri ürünleri otomatik olarak tanıyan ve toplam fiyatı gösteren akıllı alışveriş sepetleri. Bu, ödeme sürecini hızlandırarak müşterilerin bekleme sürelerini azaltabilir.

    **Self-Checkout Kioskları:** Müşterilerin kendi ödemelerini yapmalarına olanak tanıyan self-checkout kioskları, kasada oluşan kuyrukları ve bekleme sürelerini azaltmak için etkili bir çözüm olabilir.
    4. Envanter Yönetimi ve Stok Takibi:

    **Akıllı Raflar:** Ürün stoklarını otomatik olarak izleyen ve azalan stokları anında bildiren akıllı raflar. Bu sistem, ürünlerin reyonlarda sürekli olarak mevcut olmasını sağlayarak müşteri memnuniyetini artırır.

    **Otomatik Stok Yenileme Sistemleri:** Mağaza içinde bulunan RFID okuyucular ve sensörler aracılığıyla envanter hareketlerini takip edebilir ve stoklar azaldığında otomatik olarak tedarik siparişleri verebilirsiniz.

    5. Müşteri ve Personel Etkileşimi:

    **Sanal Asistanlar:** Mağaza içinde, müşterilere ürün bulmalarına, özellikleri hakkında bilgi edinmelerine veya mağaza içi kampanyalardan haberdar olmalarına yardımcı olacak yapay zeka destekli sanal asistanlar yerleştirilebilir.

    **Çalışan Yönlendirme Sistemleri:** Akıllı mağaza sistemleri, müşteri yoğunluğu olan reyonları tespit ederek personelin bu alanlara yönlendirilmesini sağlayabilir. Bu, müşteri hizmetinin hızını ve kalitesini artırır.

    6. Veri Analitiği ve Raporlama:

    **Gerçek Zamanlı Veri Analizi:** Mağaza içinde toplanan verileri gerçek zamanlı olarak analiz edebilen ve yöneticilere bu veriler doğrultusunda anında karar alma imkanı sunan veri analitiği sistemleri.

    **Tahmin Analitiği:** Müşteri davranışlarını ve satış trendlerini tahmin eden yapay zeka destekli analitik araçlar. Bu sistemler, gelecekteki talepleri öngörerek envanter yönetimi ve satış stratejilerini optimize etmek için kullanılabilir.

    7. Entegre Mağaza Yönetimi Platformları:

    **Tüm Sistemlerin Entegrasyonu:** Tüm akıllı mağaza teknolojilerini tek bir platformda entegre ederek, mağaza yöneticilerinin her şeyi merkezi bir yerden yönetmesine olanak tanıyacak entegre yönetim platformları kurulabilir. Bu, verimliliği artırır ve mağaza içi operasyonların daha sorunsuz bir şekilde yürütülmesini sağlar.

    Bu akıllı mağaza teknolojileri, müşteri memnuniyetini artırarak ve operasyonel verimliliği iyileştirerek firmanın rekabet gücünü artırabilir. Ayrıca, veri tabanlı karar alma süreçlerini geliştirerek, mağaza içi satışları ve müşteri sadakatini artırmak için değerli içgörüler sunar.
    """)
    

if selected == "Proje":
    st.title(f"Proje Yapımı")
    st.header("Mekansal Birey Kalma Süresi Analizi")
    
    st.markdown(""" Yapılan projede amaç bir alanda kamera ile alınan görüntülerden kişilerin
                 bir alan içinde ne kadar kaldığını bulmaktır. Bunun için belirlenen bir alanda kişiler
                 o alana gelince orada ne kadar kaldığını saniye olarak hesaplar. Kaç kiçi oradan geçtiyse hepsi için bunu yapar.""")

    st.subheader("İlk video kaydı")
    video1 = open("video.mov","rb")
    st.video(video1)
    st.subheader("İşlenmiş video sonucu")
    st.video('https://www.youtube.com/watch?v=UjbjPzVZkdM')
if selected == "Analiz":
    st.title(f"Proje Analizi")
    
    st.header("Mekansal Birey Kalma Süresi Analizi")
    st.markdown("Yapılan çalışmada oluşturulan veriler ile aşağıdaki analizler yapılmıştır.")
    img1=Image.open("df.png")  
    st.image(img1)
    st.subheader("1-Bar Grafiği")
    img=Image.open("bar.png")
    st.image(img, width=600, caption="Bar grafiği")
    st.markdown("""
        

**1-Bar Grafiği:**
**Veri Dağılımı:** Bu grafikte, farklı ID'lerin belirli bir alanda ne kadar zaman geçirdiği gösterilmektedir. Yükseklikler, her bir kişinin o alanda kalma süresini (saniye cinsinden) temsil ediyor.
Belirgin Zaman Farklılıkları: İlk birkaç kişi (1, 2, 3, 5, 7 numaralı ID'ler) daha uzun süreler harcarken, diğer ID'ler (12, 14 gibi) daha az zaman geçirmiş.
**Veri Sayısı:** Grafik, belirli ID'ler için veriyi göstermekte ve bunlar arasında belirgin bir fark olduğu gözlenmekte. Örneğin, 1, 2 ve 3 numaralı ID'ler yaklaşık olarak 5 saniye harcarken, diğerleri daha az zaman harcamış. """)
    st.subheader("1-Line Grafiği")
    img=Image.open("line.png")
    st.image(img, width=600, caption="Line grafiği")
    st.markdown("""
**Trend ve Dalgalanmalar:** Çizgi grafiği, her ID'nin zaman harcama eğilimini göstermektedir. İlk birkaç ID'nin zaman harcama miktarlarında bir azalma görülmekte, daha sonra düşük bir noktaya ulaşıldığında tekrar hafif bir artış gözleniyor.
**Görsel Akıcılık:** Line grafiği, zaman harcama verilerindeki dalgalanmaları daha akıcı ve net bir şekilde gösteriyor. Özellikle 5. ve 7. ID'ler arasında zaman harcamada belirgin bir azalma var.
**Belirsizlik Bantları:** Grafikteki gölgeli alanlar, verilerdeki belirsizlik veya dağılımı göstermektedir. Bu da verinin ne kadar güvenilir olduğunu veya ne kadar değişkenlik gösterdiğini anlamaya yardımcı olabilir.""")
    st.markdown("""**Genel Değerlendirme:**
Her iki grafik de belirli kişilerin bir alanda harcadığı süreler arasında önemli farklılıklar olduğunu göstermektedir.
Bar grafiği, bireysel karşılaştırmalar için iyi bir genel bakış sağlarken, çizgi grafiği zaman içinde sürelerin nasıl değiştiğini daha iyi vurguluyor.
Belirsizlik bantları, çizgi grafiğindeki veri dalgalanmalarını daha iyi anlamaya yardımcı olabilir.
Bu grafikler, farklı ID'lerin belirli bir alanda geçirdiği süredeki farklılıkları ve bu sürelerin eğilimlerini analiz etmek için kullanılabilir.""")
if selected == "Öneriler":   
    st.title(f"Öneriler")
    
    st.header("Mekansal Birey Kalma Süresi Analizi")

    img=Image.open("reyon.png")
    st.image(img, width=600, caption="örnek reyon")
    st.markdown("""

1. **Reyon Düzeni ve Yerleşim Analizi:**

**Yüksek Bekleme Süresi Olan Bölgeler:**
                
Eğer belirli bir reyonun önünde yüksek bekleme süreleri tespit ediliyorsa, bu reyonun müşteriler tarafından ilgi çektiği anlamına gelebilir. Bu tür reyonlarda ürün sergileme teknikleri geliştirilebilir veya müşteri ilgisini daha da artırmak için promosyonlar yapılabilir.

**Düşük Bekleme Süresi Olan Bölgeler:**
                
 Aksine, bazı reyonlar önünde düşük bekleme süreleri gözlemleniyorsa, bu reyonların düzeni, ürün seçimi veya yerleşiminde bir problem olabilir. Bu reyonları daha çekici hale getirmek için yeniden düzenlemeler yapılabilir veya ürünlerin yerleri değiştirilebilir.

2. Ürün ve Stok Yönetimi:

**Popüler Ürünler:**
                
 Yüksek bekleme süreleri olan reyonlar, popüler ürünlerin bulunduğu alanlar olabilir. Bu durumda, bu ürünlerin stoklarının yeterli olup olmadığı kontrol edilmelidir. Popüler ürünler için stok artırımı veya çeşitlendirme yapılabilir.

**Daha Az İlgi Gören Ürünler:**
                
 Düşük bekleme süreleri olan reyonlarda bulunan ürünlerin satış performansı düşük olabilir. Bu ürünler için indirimler veya promosyonlar düzenlenebilir, ürünlerin müşteri ilgisini çekip çekmediği analiz edilebilir. Ya da yüksek bekleme olan reyonlardaki ürünlerle yer değişikliği yapılabilir.

3. Mağaza İçi Deneyim İyileştirmeleri:

**Müşteri Akışını Yönlendirme:** Müşterilerin belirli reyonlarda uzun süre beklemesi, mağaza içinde trafik sıkışıklığına yol açabilir. Müşteri akışını daha etkin bir şekilde yönetmek için reyonların yerleşimi veya mağaza içi yönlendirme levhaları iyileştirilebilir.

**Bekleme Alanları:** Eğer müşteriler belirli reyonlar önünde çok uzun süre bekliyorlarsa, bu alanlara yakın rahat oturma alanları, bilgi ekranları veya ürün tanıtım videoları gibi müşteri deneyimini iyileştirecek unsurlar eklenebilir.

4. Personel ve Müşteri Hizmetleri:

**Personel Dağılımı:**
                
 Yüksek bekleme sürelerinin olduğu reyonlar, ekstra personel desteği gerektirebilir. Bu reyonlarda müşterilere daha hızlı ve etkili hizmet vermek için ek personel görevlendirilebilir.

**Müşteri Geri Bildirimi:**
                
 Belirli reyonlarda uzun süre bekleyen müşterilere neden bu kadar bekledikleri sorulabilir ve bu bilgiler, müşteri deneyimini iyileştirmek için kullanılabilir.

5. Reklam ve Pazarlama Stratejileri:
                
**Veri Destekli Kampanyalar:**
                
 Bekleme sürelerine göre en popüler reyonların analiz edilmesi, firma için veri odaklı pazarlama stratejileri geliştirmeye yardımcı olabilir. Örneğin, bu reyonlardaki ürünler için hedeflenmiş reklam kampanyaları düzenlenebilir.

**Müşteri Segmentasyonu:**
                
 Bekleme sürelerine göre müşterilerin hangi segmentlerinin hangi reyonlarda daha fazla zaman geçirdiği analiz edilerek, bu segmentlere yönelik özel kampanyalar oluşturulabilir.
                
6. Teknolojik Yatırımlar:
                
**Akıllı Mağaza Sistemleri:**
                
 Mağaza içi müşteri hareketlerini izleyen sensörler ve kameralar gibi teknolojiler kullanılarak, müşteri davranışları daha iyi analiz edilebilir ve bekleme süreleri daha doğru bir şekilde ölçülebilir.
 
**Self-Checkout ve Mobil Ödeme İmkanları:**
                
 Uzun bekleme sürelerini azaltmak için müşterilerin hızlı bir şekilde ödemelerini yapabilecekleri self-checkout ve mobil ödeme sistemleri teşvik edilebilir.

Bu öneriler, bekleme süreleri analizinden elde edilen verilere dayalı olarak müşteri memnuniyetini artırmak, satışları optimize etmek ve genel mağaza performansını iyileştirmek için kullanılabilir.  """)



    








# 
# img=Image.open("video.png")
# st.image(img, width=600, caption="süre ve kişiler")

# st.subheader("İlk video kaydı")
# # video1 = open("video.mov","rb")
# # st.video(video1)

# st.subheader("İşlenmiş video sonucu")

# st.video(video2)

# 