!async function () {
    const path = window.location.pathname;

    if (path === "/") {
        document.getElementById('home').classList.add("nav__item--active");
    } else if (path.includes("blogs/")) {
        document.getElementById('blogs').classList.add("nav__item--active");
    } else if (path.includes("about/")) {
        document.getElementById('about').classList.add("nav__item--active");
    }
    const loc = window.location;
    async function myScripts() {
        await fetch("https://www.googletagmanager.com/gtag/js?id=G-T4N0V6BFJR").then(response => response.text()).then(text => eval(text)).then(() => {
            window.dataLayer = window.dataLayer || [];
            function gtag() { dataLayer.push(arguments); }
            gtag('js', new Date());
            gtag('config', 'G-T4N0V6BFJR');
        })
    }
    window.addEventListener('load', async function () {
        window.cookieconsent.initialise({
            revokeBtn: "<div class='cc-revoke'></div>",
            type: "opt-in",
            theme: "classic",
            palette: {
                popup: {
                    background: "#000",
                    text: "#fff"
                },
                button: {
                    background: "#fd0",
                    text: "#000"
                }
            },
            content: {
                message: "We serve cookies on this site to analyze traffic, remember your preferences, and optimize your experience.",
                href: `/privacy-policy/`
            },
            onInitialise: async function (status) {
                if (status == cookieconsent.status.allow) await myScripts();
            },
            onStatusChange: async function (status) {
                if (this.hasConsented()) await myScripts();
            }
        })
    });

}()