(TeX-add-style-hook
 "quadratic_equation"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("scrartcl" "12pt" "a4paper" "english" "ngerman")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("inputenc" "utf8") ("fontenc" "T1") ("biblatex" "backend=biber" "autolang=other" "style=alphabetic" "citestyle=alphabetic" "giveninits=false" "") ("csquotes" "babel" "german=quotes") ("cleveref" "ngerman")))
   (TeX-run-style-hooks
    "latex2e"
    "scrartcl"
    "scrartcl12"
    "typearea"
    "iftex"
    "fontspec"
    "inputenc"
    "fontenc"
    "lmodern"
    "babel"
    "biblatex"
    "csquotes"
    "graphicx"
    "varioref"
    "cleveref"))
 :latex)

