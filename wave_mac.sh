#!/bin/bash
# Script to run wave on Mac OS
runtime/mac/jdk/bin/java --module-path runtime/mac/jfx/lib/ --add-modules javafx.controls,javafx.fxml,javafx.web -jar runtime/bin/wave > /dev/null 2>&1 &
