Escape      Meaning
\newline    Ignored (continuation line)
\\          Backslash (stores one \)
\'          Single quote (stores ')
\"          Double quote (stores ")
\a          Bell
\b          Backspace
\f          Formfeed
\n          Newline (linefeed)
\r          Carriage return
\t          Horizontal tab
\v          Vertical tab
\xhh        Character with hex value hh (at most 2 digits)
\ooo        Character with octal value ooo (up to 3 digits)
\0          Null: binary 0 character (doesn’t end string)
\N{ id }    Unicode database ID
\uhhhh      Unicode 16-bit hex
\Uhhhhhhhh  Unicode 32-bit hexa
\other      Not an escape (keeps both \ and other)

The \Uhhhh... escape sequence takes exactly eight hexadecimal digits (h); both \u and \U can be used only in Unicode string literals.

