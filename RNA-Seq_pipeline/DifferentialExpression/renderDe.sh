#!/usr/bin/env bash
# renderDe.sh
R -e "rmarkdown::render('de.Rmd', output_format='all')"
