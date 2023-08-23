(TeX-add-style-hook
 "quad_gl"
 (lambda ()
   (add-to-list 'LaTeX-verbatim-environments-local "semiverbatim")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "path")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "url")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "nolinkurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperbaseurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperimage")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "href")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "path")
   (TeX-run-style-hooks
    "../../../shared/thesis-cfg"
    "../../../shared/switch-cfg"
    "../../../shared/texts/titel_quad_gl"
    "../../../shared/figures/r_to_r_tex"
    "beamerarticle")
   (LaTeX-add-labels
    "chap:verf-los"
    "fig:r_to_t"
    "sec:vieta"
    "chap:beispielcode"))
 :latex)

