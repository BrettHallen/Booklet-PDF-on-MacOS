#!/usr/bin/env python3
"""
pdf-booklet.py
Create a booklet PDF ready for double-sided printing, 
mainly to solve the missing "Print as Booklet" layout
option in the macOS program Preview.

Usage:
python3 pdf-booklet.py input.pdf [output.pdf] [--binding left|right]

Requirements: 
pip install pymupdf

Brett Hallen, Jan 2026
"""

import sys
import argparse
import fitz     # PyMuPDF

########################
# Main worker function #
########################
def make_booklet(input_path, output_path=None, left_binding=True):
    if output_path is None:
        suffix = "-booklet-left.pdf" if left_binding else "-booklet-right.pdf"
        output_path = input_path.replace(".pdf", suffix)

    doc = fitz.open(input_path)
    # How many pages?
    n = len(doc)

    # Pad with blank pages to make multiple of 4
    if n % 4 != 0:
        blank = fitz.open()
        blank.new_page(width=doc[0].rect.width, height=doc[0].rect.height)
        for _ in range(4 - n % 4):
            doc.insert_pdf(blank)

    # Total number of pages to process
    n = len(doc) # now a multiple of 4
    # How many digits in the page count so we can dynamically format the progress output text
    page_count_width = len(str(n))  # 68 pages -> 2,  999 pages -> 3, 10000 pages -> 5
    booklet = fitz.open()

    print("\nBooklet Layout Generator (23/Jan/2026)")
    print("--------------------------------------")
    print(f">> Processing {input_path}")
    print(f">> Binding mode {'LEFT (Western)' if left_binding else 'RIGHT (Japanese)'}\n")

    # Process four pages into two new (double sided) pages each loop
    for i in range(n // 4):
        ##################
        # Front of sheet #
        ##################
        booklet.new_page(width=doc[0].rect.width * 2, height=doc[0].rect.height)
        left  = booklet[-1]
        right = booklet[-1]
        if left_binding:
            # LEFT binding: outer (high) on LEFT, inner (low) on RIGHT
            p1 = 2 * i              # left  side = high number
            p2 = n - 1 - 2 * i      # right side = low number
        else:
            # RIGHT binding: outer (high) on RIGHT, inner (low) on LEFT
            p1 = n - 1 - 2 * i      # right side = high number
            p2 = 2 * i              # left  side = low number
        print(f"   Processing pages {p1+1:>{page_count_width}} & {p2+1:>{page_count_width}} -> new page {2*i+1}")
        left.show_pdf_page(fitz.Rect(0, 0, doc[0].rect.width, doc[0].rect.height), doc, p2)
        right.show_pdf_page(fitz.Rect(doc[0].rect.width, 0, doc[0].rect.width * 2, doc[0].rect.height), doc, p1)

        #################
        # Back of sheet #
        #################
        booklet.new_page(width=doc[0].rect.width * 2, height=doc[0].rect.height)
        left  = booklet[-1]
        right = booklet[-1]
        if left_binding:
            # LEFT binding: outer (high) on LEFT, inner (low) on RIGHT
            p3 = n - 2 - 2 * i
            p4 = 2 * i + 1
        else:
            # RIGHT binding: outer (high) on RIGHT, inner (low) on LEFT
            p3 = 2 * i + 1
            p4 = n - 2 - 2 * i
        print(f"   Processing pages {p3+1:>{page_count_width}} & {p4+1:>{page_count_width}} -> new page {2*i+2}")
        left.show_pdf_page(fitz.Rect(0, 0, doc[0].rect.width, doc[0].rect.height), doc, p4)
        right.show_pdf_page(fitz.Rect(doc[0].rect.width, 0, doc[0].rect.width * 2, doc[0].rect.height), doc, p3)

    #############
    # All done! #
    #############
    booklet.save(output_path)
    print(f"\n>> Booklet PDF saved to {output_path}\n")
    print("When printing: double sided on short edge\n")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        # Not enough command line arguments
        # Print some help
        print("\n---------------------------------------------------------------")
        print("Reorganise an A4 PDF into A5 booklet format ready for printing.")
        print("This is mainly to solve the missing \"Booklet\" layout option in")
        print("Mac OS 10.15 onwards (so far still missing in macOS 26.2).\n")
        print("Default binding is left (Western).\n")
        print("Usage: python3 pdf-booklet.py input.pdf [output.pdf] [--binding left|right]")
        print("\nNote!  Requires \"pip install pymupdf\"")
        print("---------------------------------------------------------------\n")
        sys.exit(1)

    # Otherwise, let's try to parse the command line
    parser = argparse.ArgumentParser(description="Create booklet PDF for double-sided printing")
    parser.add_argument("input", help="Input PDF file")
    parser.add_argument("output", nargs="?", help="Output PDF file (optional)")
    parser.add_argument("--binding", choices=["left", "right"], default="left",
                        help="Binding side: 'left' (default, Western) or 'right' (Japanese)")

    args = parser.parse_args()

    # Let's do it!
    make_booklet(args.input, args.output, left_binding = (args.binding == "left"))
