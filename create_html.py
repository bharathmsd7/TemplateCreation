
def create_html(fileName, date, bride, groom, place, bridePhoto, groomPhoto, invitation):
    fileName = fileName.replace(' ','')
    file = fileName+".html"
    f = open(file,'w')

    message = """<!DOCTYPE html>
    <html data-wf-domain="suryawedsjyothika.webflow.io" data-wf-page="5fc72337387739d4c2d09bfe" data-wf-site="5fc72337387739573dd09bfd" data-wf-status="1">
    <head>
        <meta charset="utf-8" />
        <title>""" + fileName + """</title>
        <meta content="width=device-width, initial-scale=1" name="viewport" />
        <meta content="Webflow" name="generator" />
        <link href="css/suryawedsjyothika.webflow.022cd7376.css" rel="stylesheet" type="text/css" />
        <script src="js/webfont.js" type="text/javascript"></script>

        <script type="text/javascript">
            WebFont.load({
                google: {
                    families: ["Montserrat:100,100italic,200,200italic,300,300italic,400,400italic,500,500italic,600,600italic,700,700italic,800,800italic,900,900italic", "PT Serif:400,400italic,700,700italic", "Great Vibes:400", "Raleway:300,regular,500,600,700,800,900",
                        "Roboto:300,regular,500,700,900", "Clicker Script:regular"
                    ]
                }
            });
        </script>

        <script type="text/javascript">
            ! function(o, c) {
                var n = c.documentElement,
                    t = " w-mod-";
                n.className += t + "js", ("ontouchstart" in o || o.DocumentTouch && c instanceof DocumentTouch) && (n.className += t + "touch")
            }(window, document);
        </script>
        <link href="img/5fc75f1f394a978e1e630530_favicon-32x32.png" rel="shortcut icon" type="image/x-icon" />
        <link href="img/webclip.png" rel="apple-touch-icon" />
    </head>
    <body>
        <div data-w-id="b647b8f3-f6e2-89d4-4498-9a7480463b53" style="display:flex" class="preloader">
            <img src="img/5fc7251ddacaa55695d6934f_vhalllogo.png" loading="lazy" sizes="100vw" alt="" class="loading-image" />
            <h1 class="heading-5">Live stream your Life&#x27;s Magical Moments</h1>
        </div>
        <div class="hero-section">
            <div class="hero-container w-container">
                <div class="hero-nav-div"><img src="img/5fc7251ddacaa55695d6934f_vhalllogo.png" loading="lazy" sizes="(max-width: 479px) 37vw, (max-width: 767px) 14vw, (max-width: 991px) 109.1875px, 141px" srcset="https://uploads-ssl.webflow.com/5fc72337387739573dd09bfd/5fc7251ddacaa55695d6934f_vhalllogo-p-500.png 500w, https://uploads-ssl.webflow.com/5fc72337387739573dd09bfd/5fc7251ddacaa55695d6934f_vhalllogo.png 660w"
                        alt="" class="vhall-logo" /><a href="#contact-form" class="hero-nav-button w-button">CONTACT US</a></div>
                <div class="hero-name-div">
                    <div data-w-id="deaa141e-09cd-3387-d166-96991c2f11a7" class="header-div">
                        <p class="the-wedding-of">The Wedding of</p>
                        <h1 class="bride-header">"""+groom+"""</h1>
                        <h1 class="heading">&amp;</h1>
                        <h1 class="bride-header groom">"""+bride+"""</h1>
                        <p class="paragraph">"""+date+"""</p><a href="#live-section" class="watch-live a watch-live-btn w-button">WATCH LIVE</a></div>
                </div>
            </div>
        </div>

        <div class="groom-and-bride-section">
            <div class="bride-groom-section-bg-div">
                <div class="bride-groom-container w-container">
                    <div class="w-layout-grid grid">
                        <div data-w-id="2b4fd213-f36a-44d5-935d-802bb8f477c7" style="-webkit-transform:translate3d(0, 50px, 0) scale3d(1, 1, 1) rotateX(0) rotateY(0) rotateZ(0) skew(0, 0);-moz-transform:translate3d(0, 50px, 0) scale3d(1, 1, 1) rotateX(0) rotateY(0) rotateZ(0) skew(0, 0);-ms-transform:translate3d(0, 50px, 0) scale3d(1, 1, 1) rotateX(0) rotateY(0) rotateZ(0) skew(0, 0);transform:translate3d(0, 50px, 0) scale3d(1, 1, 1) rotateX(0) rotateY(0) rotateZ(0) skew(0, 0);opacity:0"
                            class="div-block-3"><img src='"""+groomPhoto+"""' loading="lazy" alt="" class="image-6" />
                            <p class="groom-header-copy">GROOM</p>
                            <h1 class="bride-header div">"""+groom+"""</h1>
                        </div>
                        <div data-w-id="852bd0a3-590c-280b-0fcb-ff9d20829087" style="-webkit-transform:translate3d(0, 50px, 0) scale3d(1, 1, 1) rotateX(0) rotateY(0) rotateZ(0) skew(0, 0);-moz-transform:translate3d(0, 50px, 0) scale3d(1, 1, 1) rotateX(0) rotateY(0) rotateZ(0) skew(0, 0);-ms-transform:translate3d(0, 50px, 0) scale3d(1, 1, 1) rotateX(0) rotateY(0) rotateZ(0) skew(0, 0);transform:translate3d(0, 50px, 0) scale3d(1, 1, 1) rotateX(0) rotateY(0) rotateZ(0) skew(0, 0);opacity:0"
                            class="div-block-3"><img src='"""+bridePhoto+"""' loading="lazy" alt="" class="image-6" />
                            <p class="groom-header-copy">BRIDE</p>
                            <h1 class="bride-header div">"""+bride+"""</h1>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="invitation-section">
            <div>
                <div class="invitation-container w-container">
                    <h1 data-w-id="18761273-5dd7-b2e9-03b9-a52019f3d6e4" style="-webkit-transform:translate3d(0, 50px, 0) scale3d(1, 1, 1) rotateX(0) rotateY(0) rotateZ(0) skew(0, 0);-moz-transform:translate3d(0, 50px, 0) scale3d(1, 1, 1) rotateX(0) rotateY(0) rotateZ(0) skew(0, 0);-ms-transform:translate3d(0, 50px, 0) scale3d(1, 1, 1) rotateX(0) rotateY(0) rotateZ(0) skew(0, 0);transform:translate3d(0, 50px, 0) scale3d(1, 1, 1) rotateX(0) rotateY(0) rotateZ(0) skew(0, 0);opacity:0"
                        class="heading-4">INVITATION</h1>
                    <img src='"""+invitation+"""' loading="lazy" style="-webkit-transform:translate3d(0, 50px, 0) scale3d(1, 1, 1) rotateX(0) rotateY(0) rotateZ(0) skew(0, 0);-moz-transform:translate3d(0, 50px, 0) scale3d(1, 1, 1) rotateX(0) rotateY(0) rotateZ(0) skew(0, 0);-ms-transform:translate3d(0, 50px, 0) scale3d(1, 1, 1) rotateX(0) rotateY(0) rotateZ(0) skew(0, 0);transform:translate3d(0, 50px, 0) scale3d(1, 1, 1) rotateX(0) rotateY(0) rotateZ(0) skew(0, 0);opacity:0"
                        data-w-id="99b18b6d-62e6-e1d9-9477-ec0923355104" alt="" class="image-5" />
                </div>


            </div>
        </div>

        <div id="live-section" class="live-section">
            <div class="live-container w-container">

                <h1 data-w-id="9941ca99-f532-da64-1e4d-6d5289403cc6" style="-webkit-transform:translate3d(0, 50px, 0) scale3d(1, 1, 1) rotateX(0) rotateY(0) rotateZ(0) skew(0, 0);-moz-transform:translate3d(0, 50px, 0) scale3d(1, 1, 1) rotateX(0) rotateY(0) rotateZ(0) skew(0, 0);-ms-transform:translate3d(0, 50px, 0) scale3d(1, 1, 1) rotateX(0) rotateY(0) rotateZ(0) skew(0, 0);transform:translate3d(0, 50px, 0) scale3d(1, 1, 1) rotateX(0) rotateY(0) rotateZ(0) skew(0, 0);opacity:0"
                    class="live-header">
                    WATCH LIVE
                </h1>

                <div style="padding-top:56.17021276595745%;-webkit-transform:translate3d(0, 50px, 0) scale3d(1, 1, 1) rotateX(0) rotateY(0) rotateZ(0) skew(0, 0);-moz-transform:translate3d(0, 50px, 0) scale3d(1, 1, 1) rotateX(0) rotateY(0) rotateZ(0) skew(0, 0);-ms-transform:translate3d(0, 50px, 0) scale3d(1, 1, 1) rotateX(0) rotateY(0) rotateZ(0) skew(0, 0);transform:translate3d(0, 50px, 0) scale3d(1, 1, 1) rotateX(0) rotateY(0) rotateZ(0) skew(0, 0);opacity:0"
                    id="w-node-4680bcfe29b2-c2d09bfe" data-w-id="81227654-cc82-c844-9291-4680bcfe29b2" class="w-embed-youtubevideo youtube-video">

                    <iframe src="https://www.youtube.com/embed/vbApNvaaYbc?rel=0&amp;controls=1&amp;autoplay=0&amp;mute=0&amp;start=0" frameBorder="0" style="position:absolute;left:0;top:0;width:100%;height:100%;pointer-events:auto" allow="autoplay; encrypted-media" allowfullscreen="">
                    </iframe>
                </div>

                <div data-w-id="7897e0e5-e6b3-102c-038d-92669e11ac53" style="-webkit-transform:translate3d(0, 50px, 0) scale3d(1, 1, 1) rotateX(0) rotateY(0) rotateZ(0) skew(0, 0);-moz-transform:translate3d(0, 50px, 0) scale3d(1, 1, 1) rotateX(0) rotateY(0) rotateZ(0) skew(0, 0);-ms-transform:translate3d(0, 50px, 0) scale3d(1, 1, 1) rotateX(0) rotateY(0) rotateZ(0) skew(0, 0);transform:translate3d(0, 50px, 0) scale3d(1, 1, 1) rotateX(0) rotateY(0) rotateZ(0) skew(0, 0);opacity:0"
                    class="div-block">
                    <h1 class="share-text">
                        Share
                    </h1>
                    <a href="#" class="link-block w-inline-block">
                        <img src="img/5fc73fbb4339a403d47fffef_990b7d2c2904f8cd9bc884d3eed6d003.png" loading="lazy" sizes="(max-width: 479px) 21vw, (max-width: 1439px) 50px, (max-width: 1919px) 3vw, 50px" alt="" class="image-3" />
                    </a>
                    <a href="#" class="link-block w-inline-block">
                        <img src="img/5fc7409040f5b8b3f52c2f97_logo-facebook.png" loading="lazy" alt="" class="image-3" /></a>
                    <a href="#" class="link-block w-inline-block">
                        <img src="img/5fc740f0c72e99952a71df9a_instagram-logos-png-images-free-download-2.png" loading="lazy" sizes="(max-width: 479px) 21vw, (max-width: 1439px) 50px, (max-width: 1919px) 3vw, 50px" alt="" class="image-3" />
                    </a>
                </div>
            </div>
        </div>
            <section id="contact-form" class="contact-form formbtn">
            <div class="container w-container">
                <h2 data-w-id="eb9e366c-3c99-7f9c-7c1c-26b8a11fccca" style="-webkit-transform:translate3d(0, 50px, 0) scale3d(1, 1, 1) rotateX(0) rotateY(0) rotateZ(0) skew(0, 0);-moz-transform:translate3d(0, 50px, 0) scale3d(1, 1, 1) rotateX(0) rotateY(0) rotateZ(0) skew(0, 0);-ms-transform:translate3d(0, 50px, 0) scale3d(1, 1, 1) rotateX(0) rotateY(0) rotateZ(0) skew(0, 0);transform:translate3d(0, 50px, 0) scale3d(1, 1, 1) rotateX(0) rotateY(0) rotateZ(0) skew(0, 0);opacity:0"
                    class="heading-3">CONTACT US</h2>
                <div class="w-form">
                    <form id="wf-form-Contact-Form" name="wf-form-Contact-Form" data-name="Contact Form" class="form">
                        <div data-w-id="eb9e366c-3c99-7f9c-7c1c-26b8a11fccd9" style="-webkit-transform:translate3d(0, 50px, 0) scale3d(1, 1, 1) rotateX(0) rotateY(0) rotateZ(0) skew(0, 0);-moz-transform:translate3d(0, 50px, 0) scale3d(1, 1, 1) rotateX(0) rotateY(0) rotateZ(0) skew(0, 0);-ms-transform:translate3d(0, 50px, 0) scale3d(1, 1, 1) rotateX(0) rotateY(0) rotateZ(0) skew(0, 0);transform:translate3d(0, 50px, 0) scale3d(1, 1, 1) rotateX(0) rotateY(0) rotateZ(0) skew(0, 0);opacity:0"
                            class="contact-form-grid">
                            <div id="w-node-26b8a11fccda-c2d09bfe"><input type="text" class="text-field w-input" maxlength="256" name="First-Name" data-name="First Name" placeholder="Name" id="First-Name" required="" /></div>
                            <div id="w-node-26b8a11fccde-c2d09bfe"><input type="tel" class="text-field-2 w-input" maxlength="256" name="Phone" data-name="Phone" placeholder="Phone number" id="Phone-2" required="" /></div>
                            <div id="w-node-26b8a11fcce2-c2d09bfe" class="div-block-2"><input type="email" class="text-field-4 w-input" maxlength="256" name="Email" data-name="Email" placeholder="Email" id="Email" required="" /></div>
                            <div id="w-node-26b8a11fcce6-c2d09bfe"><input type="tel" class="text-field-3 w-input" maxlength="256" name="location" data-name="location" placeholder="Location" id="location-2" /></div>
                        </div><input type="submit" value="SUBMIT" data-wait="Please wait..." data-w-id="eb9e366c-3c99-7f9c-7c1c-26b8a11fccee" style="-webkit-transform:translate3d(0, 50px, 0) scale3d(1, 1, 1) rotateX(0) rotateY(0) rotateZ(0) skew(0, 0);-moz-transform:translate3d(0, 50px, 0) scale3d(1, 1, 1) rotateX(0) rotateY(0) rotateZ(0) skew(0, 0);-ms-transform:translate3d(0, 50px, 0) scale3d(1, 1, 1) rotateX(0) rotateY(0) rotateZ(0) skew(0, 0);transform:translate3d(0, 50px, 0) scale3d(1, 1, 1) rotateX(0) rotateY(0) rotateZ(0) skew(0, 0);opacity:0"
                            class="hero-nav-button form-btn w-button" /></form>
                    <div class="w-form-done">
                        <div>Thank you! Your submission has been received!</div>
                    </div>
                    <div class="w-form-fail">
                        <div>Oops! Something went wrong while submitting the form.</div>
                    </div>
                </div>
            </div>
        </section>
        <div class="footer">
            <div data-w-id="d1cbb2d7-5bef-1347-6eee-942e88d4a4a6" style="-webkit-transform:translate3d(0, 50px, 0) scale3d(1, 1, 1) rotateX(0) rotateY(0) rotateZ(0) skew(0, 0);-moz-transform:translate3d(0, 50px, 0) scale3d(1, 1, 1) rotateX(0) rotateY(0) rotateZ(0) skew(0, 0);-ms-transform:translate3d(0, 50px, 0) scale3d(1, 1, 1) rotateX(0) rotateY(0) rotateZ(0) skew(0, 0);transform:translate3d(0, 50px, 0) scale3d(1, 1, 1) rotateX(0) rotateY(0) rotateZ(0) skew(0, 0);opacity:0"
                class="container-2 w-container">
                <img src="img/5fc7251ddacaa55695d6934f_vhalllogo.png" loading="lazy" sizes="(max-width: 479px) 32vw, (max-width: 767px) 14vw, (max-width: 991px) 109.1875px, 141px" alt="" class="image-4" />
                <div class="text-block">@ 2020 VHALL. All Rights Reserved by VHALL.</div>
            </div>
        </div>
        <script src="js/jquery-3.5.1.min.dc5e7f18c8082f.js" type="text/javascript "></script>
        <script src="js/webflow.aa605e963.js " type="text/javascript "></script>
    </body>
    </html>"""

    f.write(message)
    f.close()


