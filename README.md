# Booklet PDF on MacOS
Simple Python script to re-organise a PDF into ready-to-print booklet format on MacOS.

## The Problem
The Preview program on (perhaps) macOS 10.14 onwards no longer includes a booklet layout option.<br>

This includes at least:
- Preview 11.0 (999.4) on macOS Catalina 10.15.7
- Preview 11.0 (1113.3.1) on macOS Tahoe 26.2

On more current macOS versions there is still the option of using (gulp) Adobe Acrobat Reader but this isn't possible on older versions.<br>

Note that I've found that my venerable Brother HL-5340D printer can no longer print double-sided correctly using the "Generic PCL Laser Printer vers. 2.3" on macOS 26.2, and Brother stopped providing macOS drivers some time ago.<br>

Rather than print both sides the same orientation, it keeps flipping the reverse page.  I'll need to figure this out.<br>

## The Solution
A Python script using the PyMuPDF library to re-organise the pages into a print-ready format with two A5-sized pages per page.<br>

Print this resulting PDF file double-sided with short edge binding to get your booklet.<br>

## How To Use
You will need to have Python 3 and the PyMuPDF library installed:<br>

```
% pip3 install pymupdf
Collecting pymupdf
  Downloading pymupdf-1.26.7-cp310-abi3-macosx_11_0_arm64.whl.metadata (3.4 kB)
  Downloading pymupdf-1.26.7-cp310-abi3-macosx_11_0_arm64.whl (22.5 MB)

Installing collected packages: pymupdf
Successfully installed pymupdf-1.26.7
```

Then simply run this Python script:<br>
```
python3 pdf-booklet.py input.pdf [output.pdf] [--binding left|right]
```
If you don't specify ```output.pdf``` it will append ```_booklet``` to the input file name, i.e. ```input_booklet.pdf```.<br>
By default it will assume left/Western binding but you can optionally specify right/Japanese binding.<br>

### Example
```
% python3 pdf-booklet.py Sony_Digital_Mavica_MVC-FD95_Manual.pdf

Booklet Layout Generator (22/Jan/2026)
--------------------------------------
>> Processing Sony_Digital_Mavica_MVC-FD95_Manual.pdf
>> Binding mode LEFT (Western)
   Processing pages 1 & 68
   Processing pages 67 & 2
   Processing pages 3 & 66
   Processing pages 65 & 4
   Processing pages 5 & 64
   Processing pages 63 & 6
   Processing pages 7 & 62
   Processing pages 61 & 8
   Processing pages 9 & 60
   Processing pages 59 & 10
   Processing pages 11 & 58
   Processing pages 57 & 12
   Processing pages 13 & 56
   Processing pages 55 & 14
   Processing pages 15 & 54
   Processing pages 53 & 16
   Processing pages 17 & 52
   Processing pages 51 & 18
   Processing pages 19 & 50
   Processing pages 49 & 20
   Processing pages 21 & 48
   Processing pages 47 & 22
   Processing pages 23 & 46
   Processing pages 45 & 24
   Processing pages 25 & 44
   Processing pages 43 & 26
   Processing pages 27 & 42
   Processing pages 41 & 28
   Processing pages 29 & 40
   Processing pages 39 & 30
   Processing pages 31 & 38
   Processing pages 37 & 32
   Processing pages 33 & 36
   Processing pages 35 & 34
>> Booklet PDF saved to: Sony_Digital_Mavica_MVC-FD95_Manual-booklet-left.pdf

When printing: double sided, on (short edge)
```
### Original PDF Layout (one A4 page per sheet)
Note: Sony (very, very obviously) is a registered trademark, along with Digital Mavica, etc.  These pages are shown here simply as an example.  The original PDF, if you are looking for the MVC-FD95 manual, can be found on the Sony website.<br>

![Original PDF layout](/PDF_Original.png)

### Converted Booklet Layout (two A5 pages per sheet)

![Booklet PDF layout](/PDF_Booklet.png)



