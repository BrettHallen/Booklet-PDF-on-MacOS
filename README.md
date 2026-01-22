# Booklet PDF on MacOS
Simple Python script to re-organise a PDF into ready-to-print booklet format on MacOS.

- [YouTube video](https://youtu.be/mSsKpEZ4v3w)

## The problem
The Preview program relies on the printer driver (apparently) to determine whether it will offer you the Layout \> Booklet option.  For example my venerable Brother HL-5340D (2009) uses the "Generic PCL Laser Printer version 2.3" and slightly more recent HP Colour LaserJet M452dw (2016) uses "HP Color LaserJet M452dw-AirPrint version 4.0".  Neither of these activate Preview's booklet layout option (apparently a CUPS issue?).<br>

The solution?<br>

Simply install the manufacturer's driver.  Pffft.  Not so easy for older ... yet still perfectly working ... printers.<br>

BUT!  Reinstalling the AirPrint driver for my HP printer DID enable the "Print at Booklet" option in Preview.  After some more searching I did manage to find a current (macOS 26) driver for my HP printer which also supported booklet layout, but the Brother printer drivers stopped being updated after macOS 10.15 Catalina so I need to rely on the generic PCL driver.<br>

![HP Print as Booklet](/Preview_Print_as_booklet.png)

The HP driver I found was "HP Easy Start" vers. 2.16.0.251010 (10/Nov/2025) which installed driver "HP Color LaserJet Pro M452 version 10.4".<br> 

On more current macOS versions there is still the option of using (gulp) Adobe Acrobat Reader but this isn't possible on older versions.<br>

This works okay on my HP but my Brother can't seem to print duplex with the same orientation - the back side is inverted from the front side.  I'm guessing this is an issue with the printer driver still.<br>

## Another solution
This should work for both older Mac OS X and macOS versions (if you can install Python 3 and the required library) and for printer drivers that don't offer the booklet option.<br>

A Python script using the PyMuPDF library to re-organise the pages into a print-ready format with two A5-sized pages per page.<br>

Print this resulting PDF file double-sided with short edge binding to get your booklet.<br>

## How to use
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
If you don't specify ```output.pdf``` it will append ```-booklet-left``` (or ```-booklet-right```) to the input file name, i.e. ```<input>-booklet-left.pdf```.<br>
By default it will assume left/Western binding but you can optionally specify right/Japanese binding.<br>

### Example
```
% python3 pdf-booklet.py Sony_Digital_Mavica_MVC-FD95_Manual.pdf

Booklet Layout Generator (23/Jan/2026)
--------------------------------------
>> Processing Sony_Digital_Mavica_MVC-FD95_Manual.pdf
>> Binding mode LEFT (Western)

   Processing pages  1 & 68 -> new page 1
   Processing pages 67 &  2 -> new page 2
   Processing pages  3 & 66 -> new page 3
   Processing pages 65 &  4 -> new page 4
   Processing pages  5 & 64 -> new page 5
   Processing pages 63 &  6 -> new page 6
   Processing pages  7 & 62 -> new page 7
   Processing pages 61 &  8 -> new page 8
   Processing pages  9 & 60 -> new page 9
   Processing pages 59 & 10 -> new page 10
   Processing pages 11 & 58 -> new page 11
   Processing pages 57 & 12 -> new page 12
   Processing pages 13 & 56 -> new page 13
   Processing pages 55 & 14 -> new page 14
   Processing pages 15 & 54 -> new page 15
   Processing pages 53 & 16 -> new page 16
   Processing pages 17 & 52 -> new page 17
   Processing pages 51 & 18 -> new page 18
   Processing pages 19 & 50 -> new page 19
   Processing pages 49 & 20 -> new page 20
   Processing pages 21 & 48 -> new page 21
   Processing pages 47 & 22 -> new page 22
   Processing pages 23 & 46 -> new page 23
   Processing pages 45 & 24 -> new page 24
   Processing pages 25 & 44 -> new page 25
   Processing pages 43 & 26 -> new page 26
   Processing pages 27 & 42 -> new page 27
   Processing pages 41 & 28 -> new page 28
   Processing pages 29 & 40 -> new page 29
   Processing pages 39 & 30 -> new page 30
   Processing pages 31 & 38 -> new page 31
   Processing pages 37 & 32 -> new page 32
   Processing pages 33 & 36 -> new page 33
   Processing pages 35 & 34 -> new page 34

>> Booklet PDF saved to Sony_Digital_Mavica_MVC-FD95_Manual-booklet-left.pdf

When printing: double sided on short edge
```
### Original PDF layout (one A4 page per sheet)
Note: Sony (very, very obviously) is a registered trademark, along with Digital Mavica, etc.  These pages are shown here simply as an example.  The original PDF, if you are looking for the MVC-FD95 manual, can be found on the Sony website.<br>

![Original PDF layout](/PDF_Original.png)

### Converted booklet layout (two A5 pages per sheet)

![Booklet PDF layout](/PDF_Booklet.png)



