#!/bin/bash
# Script to run wave on Mac OS
runtime/jdk/bin/java --module-path runtime/jfx/lib/ --add-modules javafx.controls,javafx.fxml,javafx.web -jar wave.jar > /dev/null 2>&1 &
