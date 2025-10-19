/*!
 * Minimal theme switcher. Basis from Pico.css - https://picocss.com
 Defaults to system preference and is overrideable on button click.
 */

const themeSwitcher = {
  // Config
  _scheme: "auto",
  buttonsTarget: "span[data-theme]",
  buttonAttribute: "data-theme",
  rootAttribute: "data-theme",
  localStorageKey: "picoPreferredColorScheme",

  init() {
    this.scheme = this.schemeFromLocalStorage;
    this.initSwitchers();
    console.log("Theme switcher initialized. Current scheme: " + this.scheme);
  },

  get schemeFromLocalStorage() {
    return window.localStorage?.getItem(this.localStorageKey) ?? this._scheme;
  },

  get preferredColorScheme() {
    return window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
  },

  initSwitchers() {
    const buttons = document.querySelectorAll(this.buttonsTarget);
    buttons.forEach((button) => {
      button.addEventListener(
          "click",
          (event) => {
            event.preventDefault();
            console.log("Theme switcher button clicked." + " Setting scheme to: " + button.getAttribute(this.buttonAttribute));
            // Set scheme
            this.scheme = button.getAttribute(this.buttonAttribute);
          },
          false
      );
    });
  },

  set scheme(scheme) {
    if (scheme === "auto") {
      this._scheme = this.preferredColorScheme;
    } else if (scheme === "dark" || scheme === "light") {
      this._scheme = scheme;
    }
    this.applyScheme();
    this.schemeToLocalStorage();
  },

  get scheme() {
    return this._scheme;
  },

  applyScheme() {
    document.querySelector("html")?.setAttribute(this.rootAttribute, this.scheme);
  },

  schemeToLocalStorage() {
    window.localStorage?.setItem(this.localStorageKey, this.scheme);
  },
};

themeSwitcher.init();
