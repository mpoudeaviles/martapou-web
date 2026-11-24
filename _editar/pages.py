# -*- coding: utf-8 -*-
# Contenido de cada página del portfolio (copiado de martapou.com / Cargo).
# Las imágenes se escriben como F/<hash>/<nombre>; el generador las convierte
# en rutas locales dentro de /images y crea la lista de descarga.

PAGES = []

def page(slug, title, html):
    PAGES.append({"slug": slug, "title": title, "html": html})

YT = '<div class="video"><iframe src="{}" allowfullscreen loading="lazy"></iframe></div>'

# ---------------------------------------------------------------- INTERACTIVE

page("Marisa", "Marisa", r'''
<h1>1. Marisa</h1>
<i>A phygital bridge treasuring grandma’s affection beyond smartphone boundaries.</i><br>
<div class="image-gallery" data-transition="fade">
<img width="2560" height="1712" data-src="F/b8f2e17145313b644524ecf5fffeb43898f65bda90011c9d48686c874bc2ddda/DSC_0281-copia.jpg">
<img width="2560" height="1441" data-src="F/5d5031e7cdf9a448e4cf34c35067dba42f6bbba2ae477cde9cd6c34928c41109/DSC04867.jpg">
<img width="2560" height="1441" data-src="F/0b5c8fa42b75595f2a7b03e4abd628df80b519099eaaf20510bd40565cc7ef6e/DSC04985.jpg">
<img width="2560" height="1441" data-src="F/e99185adaa067ddee64e1a957aa5ca8225874c1ea769a6f43b1db6c5e14bde43/DSC04956.jpg">
</div><br>
Although my grandma and I have very different ways of interacting with our smartphones, we
both have anxieties provoked by these devices. Even so, we deal with them pursuing the
goal that these technologies promise to fulfill: keeping us connected with those we love.<br><br>However, these anxieties reflect in the design of these digital spaces a will to prioritize
retaining us in interaction over reaching our goal.
From interaction design, we wonder how a device can be generated that allows us to
transmit our affection, moving away from the smartphone, its problems, and third-party
interests. For this purpose, autoethnography has been used to understand the relationship
between users and their smartphones, their bond, and how it is transferred to the digital
environment.
<br><br>
YT:https://www.youtube.com/embed/UIhPkkhBH6c
<br>We present a pair of desks that allow users to send letters to each other instantly, using a
webcam to capture them and a robotic arm to write them, but only if they have left their
smartphone in an exterior drawer. This device represents a fusion between the analog and
the digital where we are fully aware of the interaction we carry out, being the only
beneficiaries of it, gaining agency over our relationship.<br>
<br><div class="image-gallery" data-transition="fade">
<img width="1707" height="2560" data-src="F/d6ec4c135fc8ff4d65a0d683069af57e1b483c0e56bbf5c14a12c508e2b0d214/DSC04758-Edit.jpg">
<img width="1441" height="2560" data-src="F/6ca63f5299965dd4e534ead4ea943c727e5b50fa719ba7c76493d46e33402931/DSC04789.jpg">
</div><br>
<br>
This project has resulted in a pair of cabinets, but it has gone much further, as it was only possible thanks to extensive research carried out hand in hand with my grandma. Together, we explored how different technologies have shaped our lives and how smartphones are affecting our relationships today. This is why I believe that the entire research process is as important as the final "product" presented. I'm working on publishing the full research in some way so you can review it. In the meantime, you can watch the video below, which showcases my grandma's thoughts and excerpts from the investigation. If you're interested in learning how the electronics work for the desk, how to build it, or how to reinterpret it, you can check out the repository I created during the building process <b><a href="https://little-tanker-d2e.notion.site/How-to-build-Marisa-684943c0c2f44e64813cff54f8bfc021" target="_blank">here.</a></b><br>
YT:https://www.youtube.com/embed/WkWNCalp4kU
<br><div grid-row>
<div grid-col><img width="1200" height="1600" data-src="F/e929d1395d7f3adba86b1aff7be9bc6ee01524b4d48d21716b45841153908b35/WhatsApp-Image-2025-07-26-at-19.33.21.jpeg"></div>
<div grid-col>This project was awarded with an ei! award as the best project inside the interactive design category.</div>
</div><br>
<div style="text-align: right;"><small>Final degree project<br>ELISAVA’s Interaction Design degree, 2024</small><br><small>Work by Marta Pou de Avilés.</small></div>
''')

page("no_res", "no_res", r'''
<h1>2. no_res: the reverberation of the fyp</h1>
<i>Reactive installation fueled by tiktok’s fyp</i><br>
<div class="image-gallery" data-transition="fade">
<img width="1600" height="1203" data-src="F/8bde33c680e14e65c5d914fd12db9df05948badaea8e3504ad43c0d4bb9fb9f4/2fa85f0f-364f-4b9a-9e74-e73f77da37f9-1.jpg">
<img width="3840" height="2160" data-src="F/0e0b4d389532129e5dd51a69f3d330a216687e9cc553ed9953e146a406cc9ba8/captura_video.jpg">
<img width="1920" height="1080" data-src="F/29b11edbae28861b3c83c6b0ae76e84e738fdb61365b43647f55ef8fd0ea3d00/no_res3.jpg">
<img width="1920" height="1080" data-src="F/3ba0373a8a3ff376bac49c0dda862591b767048f8ab13b974e55b5e3b50e7791/no_res5.jpg">
</div><br>
<br>
Images have escaped the screen. They encapsulate our attention, already monetized, through an algorithm designed to hold us captive. But could we inhabit them differently?<br>
<br>
YT:https://www.youtube.com/embed/iiLAPO7O2zA
“No_res” is a reactive installation fueled by TikTok’s fyp. Using a rotating cloud of mirrors, generative audio, and real-time projection, we create an immersive landscape that only becomes corrupted by the presence of phones. Images are distorted, transformed into a liminal space where the digital no longer demands but floats.<br>
<br><br>
YT:https://www.youtube.com/embed/R6dU95ITcds
<br>
<div style="text-align: right;"><small>Final master degree project<br>BAU, master in Audiovisual Innovation and interactive Installations, 2025</small><br><small>Work by Alex Sánchez, Ana Soriano and Marta Pou de Avilés.</small></div>
''')

page("A-Dialogue-with-Light-by-Antoni-Arola-copy", "A Dialogue with Light by Antoni Arola", r'''
<h1>3. A Dialogue with Light by Antoni Arola (B1F)</h1><i>Art installation by Antoni Arola inside his first solo exhibition at Karimoku Research, Tokyo</i><br>
<div class="video"><iframe src="https://player.vimeo.com/video/1140014111?h=4b840a91fb" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen loading="lazy"></iframe></div>
<br>In October 2025, Santa &amp; Cole presented the work of Antoni Arola at the KARIMOKU RESEARCH CENTER in Tokyo. This three-floor exhibition went through all the paths the artist follows in order to dialogue with light. Visitors encountered distinct perspectives through immersive installations, product design, and moments from the creative process—where light becomes matter, intuition transforms into method, and every form is an act of discovery.<br><br>
Inside this context, I got to work on the B1 Floor, dedicated to an art installation. This installation consisted of a mechanical tree that slowly rotated, caressed by a plane of light that also turned slowly. Occasionally, one of the tree’s branches would activate a sensor that would trigger the sound of a cricket, which would also affect the light. All those elements together created a beautiful and peaceful atmosphere that captivated every visitor.<br>
<br><div class="image-gallery" data-transition="fade">
<img width="2000" height="1125" data-src="F/c8cd1b833f06ce22c8be53b8ef3925e26b2ba77f6cbbc99890c4ac258f37e431/09-Masaaki-Inoue.jpeg">
<img width="2000" height="1125" data-src="F/2ec82cb5b36d6f1c246b334e37554a66b1abbf1ffeb4a186c3582a9d94ea24bd/10-Masaaki-Inoue.jpeg">
<img width="2000" height="1125" data-src="F/384e3dca630323d3da67d3c7765cdc8d6fb1f55ccc2899c67e2f62e03f1ef986/11-Masaaki-Inoue.jpeg">
</div><small><i>Photos and videos by&nbsp;Masaaki Inoue, Antoni Arola Studio</i></small><br><br>
During this time at the studio, I had the pleasure of working on all the phases of this installation’s development: from experimentation to the design and formalization. I was asked to experiment with the circular movement of this main tree figure through light and sound, which I did using different tools: projectors, lasers, video tracking or generative sound.<br>
Once its form was clear, I developed the technical aspect of the installation: from projection to the tree’s physical interaction with sound and light, as well as how everything should be implemented in the place in order to work. In order to do that, I mainly used ESP32, sensors, and Resolume, all connected through OSC.<br>
<br><br>
<div class="image-gallery" data-transition="fade" data-speed="1">
<img width="952" height="1333" data-src="F/bef6ac48ea22f056bc867d7dc0835261a793918e272cf11b326e6602a5733523/29-juliol-1.jpg">
<img width="952" height="1333" data-src="F/78bd9081891abe0a1b481a9fc6f8de482930d6012336a2fd104bbbb911636273/29-juliol-3-1.jpeg">
<img width="950" height="1330" data-src="F/4b947bf076c9e5c584ebfe18b01edc28b33733af73ea7070c4d1175aba070daf/16_septembre_test_arbre_fiat_lux_karimoku-2.jpg">
<img width="2560" height="1440" data-src="F/54f76779da73163fafec0e5465fcef87e35802a04846177d9bd541585436c6be/25-Abril-2025-2-1-scaled.jpeg">
<img width="950" height="1330" data-src="F/28e0d1f0396a86dae65a3f43c621e4d8faadbe76eaba36c0113d706a7f00d1af/22-Sep.-2025_Proves-Arbre-_-22-Sep.-2025-1.jpeg">
</div><br>
<br><br>
<div style="text-align: right;"><small><i>Project by Antoni Arola<br>Design Assistant at Antoni Arola Studio, 2025</i></small></div>
''')

page("Fiat-Lux-Zaragoza-by-Antoni-Arola", "Fiat Lux by Antoni Arola", r'''
<h1>4. Fiat Lux by Antoni Arola</h1><i>Public installation by Antoni Arola inside Zaragoza Luce Light Festival</i>
<div class="video"><iframe src="https://player.vimeo.com/video/1062765920?badge=0&amp;autopause=0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen loading="lazy" title="Fiat Lux Zaragoza, Antoni Arola"></iframe></div>
<br>“The Catalan artist's proposal is titled "Fiat Lux" and has a strong poetic charge. Arola used lasers, smoke, and interactive elements to create this installation in which the boundary between the tangible and the illusion blurs, enveloping the viewer in its journey and making them the protagonist, as they move forward, changing their surroundings.<br>
<br>
Light and space become a sensorial language with a piece tailored to the space and dimensions of Zaragoza's Roman Theater, a format never seen in any other city.<br>
<br>
The work of Arola, one of the most prominent artists in the field of light, responds to his eternal search for beauty, drawing inspiration from ancient cultures, digital codes, and chance.“&nbsp;<br>
<br><div class="image-gallery" data-transition="fade">
<img width="4032" height="2268" data-src="F/eacc26931344e764dd3c8a12ecf3d996127a9adec6154ac4d9e2fa9a2d01c86c/WhatsApp-Image-2025-07-28-at-18.21.59-2.jpeg">
<img width="1600" height="1068" data-src="F/5db30f3774aff208f85b3804e8a2d865ba7a58c91fe8e54efdd5f03229245fa3/WhatsApp-Image-2025-07-28-at-18.21.59-1.jpeg">
<img width="1600" height="899" data-src="F/a9043585ac920b6c753f0c327b73af46e3686d2aaba415f26593eae052f97ff2/WhatsApp-Image-2025-07-28-at-18.21.59.jpeg">
</div>
<br><br>
As an Intern in Arola’s studio, I had the pleasure of taking part in the adaptation of the artist’s famous installation “Fiat Lux” for the first edition of the Zaragoza’s light festival “Zaragoza Luce”. <br>My role in this project was to experiment with projector and laser programming with a model and prepare both contents and files for the final videomapping. I also got to create some of the animations using After Effects.<br>
<br><br>
<video autoplay loop playsinline muted src="VIDEO:fiat-lux-maqueta.mp4"></video>
<div style="text-align: right;"><small><img width="1920" height="2560" data-src="F/7b5cd92cd723d724231b4a1e0956dbdbe91b9c738297a4f61e102f2323b6ad9a/20-Feb.-Proves-al-teatre-roma-Zaragoza-Luce-6-1-scaled.jpeg"><br>
Project by Antoni Arola<br>Internship at Antoni Arola Studio, 2025</small></div>
''')

page("What-Streaming-Reflects", "What Streaming Reflects", r'''
<h1>5. What Streaming Reflects</h1>
<i>Public installation questioning IRL streaming</i><br>
YT:https://www.youtube.com/embed/S7R8y1tTk7c
<div style="text-align: center;"><br>
This project has its own website, which I recommend having a look at!
<b><a href="https://whatstreamingreflects.xyz/" target="_blank"><span style="color: #a76ded;">Click here.</span></a></b></div><br>
In today's digital age, feelings of loneliness and isolation have become increasingly prevalent, particularly among teenagers and young adults. Despite the perception that social media keeps us more connected than ever, harmful behaviors have emerged from certain platforms, exacerbating these feelings. Twitch, with its IRL streams, has become a breeding ground for such behaviors. Individuals lacking social skills, shyness, or insecurities have found solace in living vicariously through others' lives, seeking virtual companionship through this type of streams.<br>
<br>
Introducing 'What Streaming Reflects,' an installation designed for public spaces. A metal structure holds a mirror alongside a screen, mimicking the layout of a Twitch stream. Equipped with a camera, the installation captures the reflection in the mirror and streams it on the project's Twitch channel, with live comments displayed on the screen. The objective is to create an unsettling sense of uncertainty, blurring the line between reality and virtuality, challenging viewers with their own reflection and the accompanying comments.<br>
<br>
While there are numerous potentially harmful virtual spaces, this project aims to shed light on a lesser-known scenario, prompting a critical examination of others that may exist. By doing so, we hope to foster awareness and encourage a thoughtful approach to navigating the digital landscape.<br><br>
<br><br>
<div style="text-align: right;"><small>Final 3rd grade Transversal Project<br>3rd year of ELISAVA’s Interaction Design degree, 2023</small><br><small>Work by Luca Chemello, Abril Roca, Samanta Roman, Rosa Bolinaga and me.</small></div>
''')

page("Put", "PUT*", r'''
<h1>6. PUT*</h1>
<i>Bag that censors misogynistic terms with songs that reappropriate them.&nbsp;</i><br>
<div class="image-gallery" data-transition="slide">
<img width="3072" height="2304" data-src="F/7a8ee107fdfdb63727eccfd1f27f60ce35d40a2e9da2464739ed50910e1100ad/bolso_de-frente.png">
<img width="3072" height="2304" data-src="F/f5725416af0bed866d1d38de5d51b6ac52de05958d976526300a20258a491552/altavoz.png">
<img width="2304" height="3072" data-src="F/7aa3424b11f68aa886f8f6081ad3bf8f295ddd5ddbe592a0b7741b8b4b6aed36/micro-bolso.png">
</div><br>
If we take a look at Spotify's top 50, we can observe how normalized misogynistic discourses are, with a majority of cisgender men singing about asses, whores, breasts, and bitches.<br>
<br>
Both this music and its use of language are everywhere, spreading a harmful message. In the face of this problem, I present a critical artifact in the form of a bag capable of identifying certain terms used in song lyrics and even street harassment, and censoring them. Through a microphone, it detects derogatory terms and then loudly plays a song where a female singer uses the same term but recontextualizes it in a positive way.<br>
<br>
The main objective of this proposal is to censor misogynistic discourses and raise awareness about their existence. The element of surprise and humor are strategically employed to grab attention and blatantly interrupt harmful speech.<br>
<br>
<div class="image-gallery" data-transition="slide">
<img width="1314" height="1066" data-src="F/f43009974c38c970067091711391fd1b5fdc3897a2754bede8f68388bfc5ccd8/calle_bolso.png">
<img width="2161" height="2916" data-src="F/0e4cb137c1527a333acfd2186beb7175772591d8be5d65d1ef92ee03433d5e4f/vicky_altavoz.png">
<img width="4000" height="4000" data-src="F/31a4bedb29d97bd267157cbd5e250e1fe4ce88633afb1c23cd4913fb302647df/vicky_y_bolso.png">
</div><br>
From mid-May to mid-June 2023, this project was exhibited in the collective art exhibition called <span style="color: #a76ded;"><b><a href="https://lift.bio/307persones558m3" target="_blank">“307 persones en 558 m3”,</a> </b><span style="color: #fff;">which I participated in organizing.</span></span><br>
<br>
<div class="image-gallery" data-transition="slide">
<img width="799" height="533" data-src="F/3f68797d1d551e4204aa48f6d1d12e955374d78d26fdb07ab8c2f3b5195addd9/52968881123_6b84a24754_c.jpg">
<img width="799" height="533" data-src="F/5cb7d3642526cb627c50ff12009bb17e7796b55c7d9b5bd108234c00f6868184/52967825877_82b4859e2d_c.jpg">
</div><br>
If you are interested in learning more about this project, you can click <span style="color: #a76ded;"><b><a href="https://www.notion.so/Put-237af7288a444b09940362a65a3749f7?pvs=4" target="_blank">here</a></b> </span>to access additional information, including references, inspiring texts, research findings, as well as the code, tutorials, and schematics for creating a similar system yourself.<br>
<br>
<div grid-row>
<div grid-col class="v-center">You can also have a look at the fanzine I did of the project by clicking the image. (Spanish only)</div>
<div grid-col><a href="https://online.fliphtml5.com/krujh/afqq/" target="_blank" class="image-link"><img width="1104" height="1550" data-src="F/0ada8dc23780740f974c19e02a582a9ad146d480c5a85d792550da56ac54f6a4/Captura-de-pantalla-2023-07-17-a-las-14.51.41.png"></a></div>
</div><br>
<br>
<div style="text-align: right;"><small>Project for my “Internet Mining” subject<br>3rd year of ELISAVA’s Interaction Design degree, 2022</small></div>
''')

page("Byte-sleeve", "Byte Sleeve", r'''
<h1>7. Byte Sleeve</h1>
<i>A wearable for environment and identity control</i><br>
<br>
<div class="image-gallery" data-transition="slide">
<img width="1080" height="1620" data-src="F/4b38af970e35736441937394a5837940b489aef37cd920d304c6bece7f77b20b/5.png">
<img width="4000" height="6000" data-src="F/f1a521f2776727a74b8305bd6aa3c30cbf755dae2c2d51ed29c1feba0d7535da/3.png">
<img width="3456" height="5184" data-src="F/8dd2b540bc96dbb706fa37fa93c54e2b50e96faaf2f6299fcc4ae2d94349a96a/1.png">
</div><br>Set in a dystopian future dated 2100, environmental conditions have been worsening, reaching scorching temperatures and high levels of UV radiation. In addition, economic protectionism increased control of borders, resources, and the population, in general, have been consolidated.<br>
<br>
We propose a wearable designed to be used both outdoors and underground, facilitating safe movement. The machine warns us of the fluctuation of the different harmful values that it is programmed to analyze: temperature, humidity, and UV; through LEDs and vibration. If it detects that any value reaches dangerous levels for health, an alarm system is activated. This information is stored and can be accessed through an NFC sensor.<br>
<br>
<div class="image-gallery" data-transition="slide">
<img width="6000" height="4000" data-src="F/ba455375a31c680f4c1f4708980ae188499e0111eea8491d5edf83c1bcc4e11f/4.png">
<img width="1440" height="1080" data-src="F/ff07250d7a3ead836683d6da9fdde0df5c8c4794f9a4ae9ae0f69501c00f0925/6.png">
</div>
<br><br>
YT:https://www.youtube.com/embed/MJAKZaiS1Vg
<br>
It is a dystopian future we are projecting; however, it could be plausible. Moreover, nowadays, this prototype plus some functional modifications could be used in different fields related to health.<br>
<br><br>
<img width="3888" height="5184" data-src="F/5c564b432b9f7ce76a7c18b58aaccd923b0b1c00d8179abb92efdf865edb09cf/2.png"><br>
Click <b><a href="https://github.com/AndiePuentes/Byte-sleeve.git" target="_blank"><span style="color: #a76ded;">here</span></a> </b>to visit the project’s GitHub repository, with the code used for programming the lilypad that runs Byte Sleeve.<br>
<div style="text-align: right;"><br>
<small>Assignment for my “Tangible experiences” class<br>2nd year of ELISAVA’s Interaction Design degree, 2022<br>Project made with Andie Puentes, Samanta Román and Fabiola Choucair.</small></div>
''')

page("Oscilloscope-game", "Oscilloscope Game", r'''
<h1>8. Oscilloscope Game</h1>
<i>Game design and production for an escape room.</i><br><br>
YT:https://www.youtube.com/embed/f_KxfyEuGrQ
<br>
We were tasked with creating a tangible game for an Escape Room centered around an Oscilloscope. Our challenge was to modify it so users could interact with it, all within a narrative that aligned with the escape room's storyline.<br>
<br>
Given that the escape room revolved around time travel, we conceptualized a game where players had to generate an infinite shape on the oscilloscope's screen to initiate time travel. To achieve this, we integrated three key components: the oscilloscope itself, a fabricated interface for user interaction, and a poster displaying various shapes and codes. Additionally, we incorporated the room's lighting system as part of the gameplay.<br>
<br>
<img width="1920" height="1080" data-src="F/47b39255e3e2c06eb474704d1af67d7471f9b2e897d576d3a89fe9e7539b2163/013-1.png"><br>
<br><br>
The poster, positioned in front of the player, showcased different shapes achievable by adjusting potentiometers on the fake interface we devised. The objective was for players to recreate the infinite shape, symbolizing time travel, which was recurrent throughout the escape room's theme. Upon successfully forming the shape, all room lights would flash, signaling the activation of the time portal.<br>
<br>
<img width="4272" height="2848" data-src="F/bf765a493d56d74493dd529043a33e4b42d3711c79085495f5331901b02c1493/_MG_9069.JPG"><br>
<br><br>
To realize this concept, we utilized Arduino to generate signals interpreted by the oscilloscope as drawings, as well as to provide an interactive interface with potentiometers. Furthermore, for managing the room's lights, we employed Max MSP.<br>
<br>
Lastly, we constructed the entire set to immerse users in the ambiance of a mad scientist's office, facilitating the recording of a demo video.<br>
<br>
<div grid-row>
<div grid-col><img width="1944" height="2592" data-src="F/0b1653f6f10196e6307d922a0c64fc572f4044d85e38487c5113d05f413f1953/IMG_0895.JPG"></div>
<div grid-col><img width="1044" height="1534" data-src="F/2d22c0a9ad2109cf973fabb8d3924ff88f91bcbc66f023fcac4144a959c498b5/oscilloscope_Victoria-Gerard-Andie-Samanta-Marta.jpg"></div>
</div><br><br>
<br>
<div style="text-align: right;"><small>Game design and production for my “Interactive interfaces” class<br>3rd year of ELISAVA’s Interaction Design degree, 2023</small><br><small>Project by Gerard Escolies, Samanta Román, Andie Puentes, Victoria Stupai and Marta Pou de Avilés.</small></div>
''')

page("View-all", "View all", r'''
<h1>View all</h1><br>
<div class="image-gallery" data-transition="fade">
<a href="PAGE:Marisa" class="image-link"><img width="2560" height="1712" data-src="F/5c8d682aa5fcffc6a4d96e5f4f0f4a012a40da33e613fcd37e6269fad444c130/DSC_0281-copia.jpg"></a>
<a href="PAGE:no_res" class="image-link"><img width="1600" height="1203" data-src="F/af9cb2b1f50afb6d8100346a934a3a4c45d41d4f52aebffa6ba4c0a7296263a6/2fa85f0f-364f-4b9a-9e74-e73f77da37f9.jpg"></a>
<a href="PAGE:A-Dialogue-with-Light-by-Antoni-Arola-copy" class="image-link"><img width="2000" height="1125" data-src="F/225ce6f0a23b6634522fe221b763dd28d31f34c10856c7160d56312fd2dcada1/11-Masaaki-Inoue.jpeg"></a>
<a href="PAGE:Fiat-Lux-Zaragoza-by-Antoni-Arola" class="image-link"><img width="1000" height="600" data-src="F/734190ee6536ba466a35e2b76b36ff7c2749f5fe09322a2f0f3fc21514d12960/fiat_lux.jpg"></a>
<a href="PAGE:What-Streaming-Reflects" class="image-link"><img width="3176" height="1890" data-src="F/e2790c89cbc4ea1ca9078c61414b30d8e924f681ab02187a0398324bdc9e8899/Capture-decran-2023-06-15-a-22.26.22.png"></a>
<a href="PAGE:Put" class="image-link"><img width="1314" height="1066" data-src="F/5d56a55f67fb8a3dffbb6febf59efad6f5089a2f3d56cb5f5de7e38db2a5cddf/calle_bolso.png"></a>
<a href="PAGE:Byte-sleeve" class="image-link"><img width="1080" height="1620" data-src="F/06d29a4093d0ade2061444032b4bcf0c21646283196075a91aba30a6a40a0947/5.png"></a>
<a href="PAGE:Oscilloscope-game" class="image-link"><img width="1920" height="1080" data-src="F/99006644710802eb7689c734c63446161697a6aa9680bc4c208fd533625daf8a/013-1.png"></a>
<a href="PAGE:Wallart-for-MCB" class="image-link"><img width="3970" height="2978" data-src="F/b66a9da894e26e5924c55c5dcdbba0bea5145d36ad4a405e98ee717a826700d4/20220203_095538-min.png"></a>
<a href="PAGE:Sour-Candy" class="image-link"><img width="2049" height="2928" data-src="F/13d3a586e8490453388979d11bd56658e06f564bd8b4e76f00cb43daa79dc6b5/784BE02B-95FB-406B-A4F7-8B96570645E0.jpeg"></a>
<a href="PAGE:Sour-Candy" class="image-link"><img width="1543" height="2183" data-src="F/39caab35ed84ab99989badb2fb7a6b94f9c0331496591fb94722dbcc3ee263dc/Miku.jpg"></a>
<a href="PAGE:Suspiria" class="image-link"><img width="2224" height="1668" data-src="F/b7d60256ab2fe97da73ea5ac3fd272c5feb7f0669dd16ed1a2418eeb2936375d/IMG_1826.PNG"></a>
<a href="PAGE:Design-for-Cataris-by-Marisol" class="image-link"><img width="1754" height="2481" data-src="F/4ce69d18af3e8f769f8db548341cfaf726cbbbee60f6000385c7933c0949bd38/catarsis-print.png"></a>
<a href="PAGE:Alix-y-Jonah" class="image-link"><img width="2248" height="2248" data-src="F/f90899e058217938cb0f28b96488180caed93a730503fda4f20abb28f633a799/Alix---Jonah_page-0001.png"></a>
<a href="PAGE:Mood-project" class="image-link"><img width="1328" height="1328" data-src="F/6df367130681a25cda101e8fbf2620f35646773c0dcc7ac5ac345d295bfeb341/Captura-de-pantalla-2022-02-24-a-las-9.56.53.png"></a>
</div><br>
''')

# ----------------------------------------------------------------------- INFO

page("Info", "Info", r'''
<br>
<h2 class="info-title">Hi! Nice to meet you</h2>
<br>
<div grid-row>
<div grid-col><img width="686" height="1116" data-src="F/d644605c8335d53723f96c682f71a105560d1a6dfbf35737b71b35f827f98318/Captura-de-pantalla-2022-05-02-a-las-22.02.31-2.png"></div>
<div grid-col><h1>Let me introduce myself:</h1>
During the last few years at university I have created projects that have helped me develop a <b>critical eye</b>, <b>attention to the user</b> and <b>aesthetic sensitivity</b>. On my own, I have been participating whenever I can in <b>group projects</b>, from things related to music and its visual communication to event organization.<br>
<br>
I consider that my strengths when approaching a project are <b>transversality, organizational capacity and ease and curiosity in learning</b>. I enjoy working in a team and feel especially comfortable in organizational or conceptualization roles. I am looking to take part in projects where I can apply my skills and evolve them, with a great interest in those related to&nbsp;<b>interactive installations or creative direction</b>.<br>
<br>
<h1>Extra facts:</h1>Beyond design,<b> I love</b>…<br>·<b>Music</b>, listening and making it.<br>·<b>Taking pictures</b>, especially of friends and events.<br>·<b>Makeup and fashion</b>, particularly into DIY culture.<br>
<br><h1>And what about you?</h1>I am always looking to participate in new projects! If you like what you see, you can contact me through&nbsp;<b><a class="accent" href="https://www.instagram.com/marta.pout/" target="_blank">instagram</a></b> or <b><a class="accent" href="mailto:m.poudeaviles@gmail.com">mail.</a></b><br>
You can also download my CV <b><a class="accent" href="https://drive.google.com/file/d/1_FLdPH53a7zlAuQzWgG1-084Dn6P56fQ/view?usp=sharing" target="_blank">here.</a></b>
</div></div>
''')

# ------------------------------------------------------------------ HOME
# Columna de imágenes que se desplaza sola (como en Cargo)

HOME = [
    ("no_res", 1600, 1203, "F/f43a0a3bbe9ca323767ea65787352df7c69af0f628d9f5661acae4004a210ffb/2fa85f0f-364f-4b9a-9e74-e73f77da37f9.jpg"),
    ("A-Dialogue-with-Light-by-Antoni-Arola-copy", 2000, 1125, "F/0249c538cd38e6c01ac7f8bc96c4422aaa4574fc09f4f0f72802b5fcfd2903d3/11-Masaaki-Inoue.jpeg"),
    ("Marisa", 1441, 2560, "F/cf27d135ace82ed910ffde860a05a9c045f0facf0778bea874cb81a4186ac13b/DSC04789.jpg"),
    ("Fiat-Lux-Zaragoza-by-Antoni-Arola", 1000, 600, "F/c0d876a72db2cb1f982019fd5b3058651a8be63bb8a321fbbd1ae7d2be5bc128/fiat_lux.jpg"),
    ("Put", 1314, 1066, "F/61ae6bf31f121354fd48d1ffe343cea5b725b5148e7549d07220627ec0eb2361/calle_bolso.png"),
    ("Byte-sleeve", 1080, 1620, "F/3c532108a14f118bce3e7ebfd2f2039d8e85f458d5b37b7a712cf2ec9853d9d2/5.png"),
    ("What-Streaming-Reflects", 3176, 1890, "F/e2790c89cbc4ea1ca9078c61414b30d8e924f681ab02187a0398324bdc9e8899/Capture-decran-2023-06-15-a-22.26.22.png"),
    ("Oscilloscope-game", 1920, 1080, "F/99006644710802eb7689c734c63446161697a6aa9680bc4c208fd533625daf8a/013-1.png"),
    ("Alix-y-Jonah", 2248, 2248, "F/f90899e058217938cb0f28b96488180caed93a730503fda4f20abb28f633a799/Alix---Jonah_page-0001.png"),
    ("Sour-Candy", 2049, 2928, "F/76beb270d2957f5c9dba1c866ff62da83d8433d4eeaa998c3b34cd2aa51a5443/784BE02B-95FB-406B-A4F7-8B96570645E0.jpeg"),
    ("Sour-Candy", 1543, 2183, "F/02016c3e1c672fc6b11ab2fa78bc26402d1c15f1f92856d48e9b1564a4b5c604/Miku.jpg"),
    ("Suspiria", 2224, 1668, "F/20a5f3e9cf372a1db4ffd76e60c2067dd072a85925d4059b8607a0626cd81202/IMG_1826.PNG"),
    ("Design-for-Cataris-by-Marisol", 1754, 2481, "F/5f047bff44946edc44fd2c69ae893e5e2c5546235ac7e052d80108de8641c33e/catarsis-print.png"),
]

VIDEOS = {
    "fiat-lux-maqueta.mp4": "https://files.cargocollective.com/c1393299/-Scale-model-for-the-project-we-presented-in--festival_luce-a-few-weeks-ago-in-Zaragoza--Project--online-video-cutter.com-.mp4",
}


# ------------------------------------------------- INFO: tres propuestas
PHOTO = '<img width="686" height="1116" data-src="F/d644605c8335d53723f96c682f71a105560d1a6dfbf35737b71b35f827f98318/Captura-de-pantalla-2022-05-02-a-las-22.02.31-2.png">'
CONTACT = ('<a href="mailto:m.poudeaviles@gmail.com">m.poudeaviles@gmail.com</a>'
           '<a href="https://www.instagram.com/marta.pout/" target="_blank">Instagram</a>'
           '<a href="https://www.linkedin.com/in/marta-pou-de-avil%C3%A9s-tarragona-5109921a4/" target="_blank">LinkedIn</a>'
           '<a href="https://drive.google.com/file/d/1_FLdPH53a7zlAuQzWgG1-084Dn6P56fQ/view?usp=sharing" target="_blank">CV</a>')

# A — texto grande, casi un manifiesto
page("Info-a", "Info", r'''
<div class="info-a">
<p class="big">Interaction designer based in Barcelona. I make <em>light</em>, <em>sound</em> and <em>objects</em> respond to people, from the first sketch to the last cable.</p>
<p class="big dim">Currently designing installations and objects at Estudi Antoni Arola, and taking on my own projects and technical commissions.</p>
<div class="contact-big">''' + CONTACT + '''</div>
</div>
''')

# B — ficha técnica
page("Info-b", "Info", r'''
<div class="info-b">
<h2 class="hello">Hi, I’m Marta.</h2>
<div class="sheet">
<div class="photo">''' + PHOTO + '''</div>
<dl>
<dt>Now</dt><dd>Designer at Estudi Antoni Arola, Barcelona</dd>
<dt>I make</dt><dd>Interactive installations, light pieces, critical objects and wearables</dd>
<dt>With</dt><dd>ESP32 · Arduino · sensors · OSC · Resolume · Max MSP · projection &amp; lasers</dd>
<dt>Recent</dt><dd><a href="PAGE:A-Dialogue-with-Light-by-Antoni-Arola-copy">A Dialogue with Light</a>, Tokyo 2025 · <a href="PAGE:Fiat-Lux-Zaragoza-by-Antoni-Arola">Fiat Lux</a>, Zaragoza 2025 · <a href="PAGE:no_res">no_res</a>, 2025</dd>
<dt>Award</dt><dd>ei! award, best interaction design project, for <a href="PAGE:Marisa">Marisa</a> (2024)</dd>
<dt>Studied</dt><dd>MA Audiovisual Innovation &amp; Interactive Environments, BAU · BA Design (Interaction), ELISAVA</dd>
<dt>Contact</dt><dd class="contact-inline">''' + CONTACT + '''</dd>
</dl>
</div>
</div>
''')

# C — bloque amarillo, en la línea de la pegatina y el anillo
page("Info-c", "Info", r'''
<div class="info-c">
<div class="card">
<p class="hey">Hi!</p>
<p class="lead">I’m Marta, an interaction designer from Barcelona. I make installations and objects where light, sound and people talk to each other.</p>
<p class="tags"><span>interaction</span><span>light</span><span>sound</span><span>art</span><span>design</span><span>technology</span><span>movement</span></p>
<p class="small">Designer at Estudi Antoni Arola. Open to my own projects, collaborations and technical commissions.</p>
<p class="cta">Let’s make something →</p>
<div class="contact-card">''' + CONTACT + '''</div>
</div>
<div class="polaroid">''' + PHOTO + '''</div>
</div>
''')

# D — palabras grandes
page("Info-d", "Info", r'''
<div class="info-d">
<ul class="words">
<li>Installations</li><li class="o">Objects</li><li>Light</li><li class="o">Sound</li><li>Interaction</li>
</ul>
<div class="side">
<p>I’m Marta, an interaction designer in Barcelona. I design and build installations and objects that react to people, from the idea to the electronics, the code and the setup.</p>
<p>Designer at Estudi Antoni Arola. Own projects and technical commissions.</p>
<div class="contact-list">''' + CONTACT + '''</div>
</div>
</div>
''')

# E — preguntas y respuestas
page("Info-e", "Info", r'''
<div class="info-e">
<div class="qa"><p class="q">What do you make?</p><p class="a">Interactive installations and objects: light pieces, <a href="PAGE:Put">critical objects</a>, <a href="PAGE:Byte-sleeve">wearables</a> and things that only work when you are there.</p></div>
<div class="qa"><p class="q">How?</p><p class="a">From the first sketch to the last cable: concept, prototypes, electronics, code and setup. ESP32, sensors, OSC, Resolume, projection and lasers.</p></div>
<div class="qa"><p class="q">Where?</p><p class="a">Barcelona. Designer at Estudi Antoni Arola, plus my own projects and technical commissions.</p></div>
<div class="qa"><p class="q">Shall we?</p><p class="a contact-list">''' + CONTACT + '''</p></div>
</div>
''')

# F — foto grande con pegatina
page("Info-f", "Info", r'''
<div class="info-f">
<div class="hero">''' + PHOTO + '''<span class="hi-sticker">Hi! I’m Marta</span></div>
<p class="line">Interaction designer in Barcelona. Installations and objects made of light, sound and electronics.</p>
<div class="cols">
<div><h3>Installations</h3><p><a href="PAGE:no_res">no_res</a> · <a href="PAGE:A-Dialogue-with-Light-by-Antoni-Arola-copy">A Dialogue with Light</a> · <a href="PAGE:Fiat-Lux-Zaragoza-by-Antoni-Arola">Fiat Lux</a></p></div>
<div><h3>Objects</h3><p><a href="PAGE:Marisa">Marisa</a> · <a href="PAGE:Put">PUT*</a> · <a href="PAGE:Byte-sleeve">Byte Sleeve</a></p></div>
<div><h3>Now</h3><p>Designer at Estudi Antoni Arola. Open to commissions and collaborations.</p></div>
</div>
<div class="contact-list">''' + CONTACT + '''</div>
</div>
''')
