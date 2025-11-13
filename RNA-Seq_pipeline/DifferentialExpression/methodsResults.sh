#!/usr/bin/env bash
# methodsResults.bash

R -e "rmarkdown::render('methodsResults.Rmd', output_format='all')"
