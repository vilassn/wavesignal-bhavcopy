# WaveSignal

WaveSignal is a technical analysis software with features like charting, back-testing, scanning of stocks/futures, and free quotes features. It is developed by νίĻάş ήίήάώέ to learn and improve trading skills.

## Features of Software

1. Practice technical analysis on historical data.
2. Generate buy/sell signals from live data using popular strategies.
3. Maintain practice and live records.
4. Backtest trading strategies.
5. Free EOD (End of Day) data feed from NSE (National Stock Exchange).
6. Live data feed from NSE, Yahoo, ETimes, and more.

Visit the website for more information: [WaveSignal Website](https://sites.google.com/view/wavesignal)

## Getting Started

To run WaveSignal, you need to have Java and JavaFX installed. You can download them from the following links:

- [Download Java](https://jdk.java.net/21/)

  - [Linux](https://download.java.net/java/GA/jdk21.0.1/415e3f918a1f4062a0074a2794853d0d/12/GPL/openjdk-21.0.1_linux-x64_bin.tar.gz)
  - [macOS](https://download.java.net/java/GA/jdk21.0.1/415e3f918a1f4062a0074a2794853d0d/12/GPL/openjdk-21.0.1_macos-x64_bin.tar.gz)
  - [Windows](https://download.java.net/java/GA/jdk21.0.1/415e3f918a1f4062a0074a2794853d0d/12/GPL/openjdk-21.0.1_windows-x64_bin.zip)

- [Download JavaFX](https://jdk.java.net/javafx21/)

  - [Linux](https://download.java.net/java/GA/javafx21.0.1/e5ab43c6aed54893b0840c1f2dcfca4d/GPL/openjfx-21.0.1_linux-x64_bin-sdk.tar.gz)
  - [macOS](https://download.java.net/java/GA/javafx21.0.1/e5ab43c6aed54893b0840c1f2dcfca4d/GPL/openjfx-21.0.1_macos-x64_bin-sdk.tar.gz)
  - [Windows](https://download.java.net/java/GA/javafx21.0.1/e5ab43c6aed54893b0840c1f2dcfca4d/GPL/openjfx-21.0.1_windows-x64_bin-sdk.zip)

## Running WaveSignal

Use the following commands to run WaveSignal on different platforms:

### Windows

```bash
start runtime\\win\\jdk\\bin\\javaw.exe --module-path runtime\\win\\jfx\\lib --add-modules javafx.controls,javafx.fxml,javafx.web -jar runtime\\bin\\wave
```

### Linux

```bash
runtime/linux/jdk/bin/java --module-path runtime/linux/jfx/lib --add-modules javafx.controls,javafx.fxml,javafx.web -jar runtime/bin/wave
```

### macOS

```bash
runtime/mac/jdk/bin/java --module-path runtime/mac/jfx/lib/ --add-modules javafx.controls,javafx.fxml,javafx.web -jar runtime/bin/wave
```

Enjoy using WaveSignal for your technical analysis and trading needs!

---

*Note: Please make sure you have the necessary Java and JavaFX installations before running WaveSignal.*
