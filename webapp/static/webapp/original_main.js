!async function () {
    const path = window.location.pathname;

    if (path === "/") {
        document.getElementById('home').classList.add("nav__item--active");
    } else if (path.includes("blogs/")) {
        document.getElementById('blogs').classList.add("nav__item--active");
    } else if (path.includes("about/")) {
        document.getElementById('about').classList.add("nav__item--active");
    }
    await fetch("https://www.googletagmanager.com/gtag/js?id=G-T4N0V6BFJR").then(response => response.text()).then(text => eval(text)).then(() => {
        window.dataLayer = window.dataLayer || [];
        function gtag() { dataLayer.push(arguments); }
        gtag('js', new Date());
        gtag('config', 'G-T4N0V6BFJR');
    })

}()