CSS3-Syntax
===========

Sublime Text 3 package for CSS3 syntax highlighting.

## Features
* __Comprehensive__: complete support for CSS3, based on the latest draft
  specs. support for many vendor-prefixed CSS extensions (e.g. -moz-, -ms-,
  -webkit-)
* __Forward-looking__: supports upcoming features like variables, CSS animation,
  and @supports.
* __Modern__: flags deprecated/obsolete parts of CSS
* __Faithful__: extremely close adherence to the spec, with minor deviations
  due to technical limitations (non-trivial deviations described [below](http://www.google.com))

## Installation
1. [Install Package Control](https://sublime.wbond.net/installation)
2. _Mac_: Cmd+Shift+P → Package Control: Install Package → CSS3 Syntax<br>
   _Windows/Linux_: Ctrl+Shift+P → Package Control: Install Package → CSS3 Syntax
3. Open .css file
4. _Mac_: Cmd+Shift+P → Set Syntax: CSS3<br>
   _Windows/Linux_: Ctrl+Shift+P → Set Syntax: CSS3

## Limitations
* Will not color these prefixes
<table>
    <tr>
        <td>-ah-</td>
        <td>-apple-</td>
        <td>-atsc-</td>
        <td>-hp-</td>
        <td>-ibooks-</td>
    </tr>
    <tr>
        <td>-khtml-</td>
        <td>-mso-</td>
        <td>-o-</td>
        <td>-prince-</td>
        <td>-rim-</td>
    </tr>
    <tr>
        <td>-ro-</td>
        <td>-tc-</td>
        <td>-weasy-</td>
        <td>-xv-</td>
        <td></td>
    </tr>
</table>

* Incomplete support for vendor-prefixed CSS extensions (We're adding
  more as we find them.)

## Deviations from the Spec
* IMPORTANT: You must end every property declaration with a semicolon
  for it to be highlighted properly. CSS does not require this, but
  it is a good practice. The semicolon helps the syntax highlighter
  distiguish between properties and values, and thus avoid applying
  the wrong coloring when the names are the same.<br>
  ```
  /* not colored */
  h1 {color: blue}
  ```

  ```css
  /* colored */
  h1 {color: blue;}
  ```
* The spec says that HTML tags, properties, values, function names,
  and more should be matched case-insenstively. This syntax highlighter
  matches only lowercase text, case-sensitively. The code below is
  legal CSS, but will not be matched by this highlighter.
  ```
  /* not colored */
  BODY LI A:HOVER {
    COLOR: RED;
  }

  ```
  ```css
  /* colored */
  body li a:hover {
    color: red;
  }
  ```
  If enough people want to write all-caps CSS, we will change the
  matching to case-insensitive. There will be a small performance
  cost.
