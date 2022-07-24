Naming
======

Library Naming
--------------

Libraries in the Google open source PDKs are named using the following scheme;

  :lib_process:`<Process name>` _ :lib_src:`<Library Source Abbreviation>` _ :lib_type:`<Library Type Abbreviation>` [_ :lib_name:`<Library Name>`]

All sections are **lower case** and separated by an **underscore**. All sections must start with an alpha character (they must not start with a number).

The sections are;

- The :lib_process:`Process name` in is the name of the process technology.

- The :lib_src:`Library Source Abbreviations` is a short abbreviation for who created and is responsible for the library. The table below shows the current list of :lib_src:`Library Source Abbreviations`;

  +----------------------------+----------------------------------------+
  | Library Source             | :lib_src:`Library Source Abbreviation` |
  +============================+========================================+
  | Technology's foundry       | :lib_src:`fd`                          |
  +----------------------------+----------------------------------------+
  | Efabless                   | :lib_src:`ef`                          |
  +----------------------------+----------------------------------------+
  | Oklahoma State University  | :lib_src:`osu`                         |
  +----------------------------+----------------------------------------+

- The :lib_type:`Library Type Abbreviation` is a short two letter abbreviation for the type of content found in the library. The table below shows the current list of :lib_type:`Library Type Abbreviations`;

  +--------------------------------+---------------------------------------+
  | Library Type                   | :lib_type:`Library Type Abbreviation` |
  +================================+=======================================+
  | Primitive Cells                | :lib_type:`pr`                        |
  +--------------------------------+---------------------------------------+
  | Digital Standard Cells         | :lib_type:`sc`                        |
  +--------------------------------+---------------------------------------+
  | Build Space (Flash, SRAM, etc) | :lib_type:`sp`                        |
  +--------------------------------+---------------------------------------+
  | IO and Periphery               | :lib_type:`io`                        |
  +--------------------------------+---------------------------------------+
  | Miscellaneous                  | :lib_type:`xx`                        |
  +--------------------------------+---------------------------------------+

- The :lib_name:`Library Name` is an optional short abbreviated name used when there are multiple libraries of a given type released from a single :lib_src:`library source`. If only one library of a given type is going to ever be released, this can be left out.
