HTML (Hypertext Markup Language) is the standard language used to create web pages. Since many websites contain valuable data (like prices, statistics, or articles), understanding HTML helps in extracting information using Python for web scraping.

### Key Concepts Covered

#### 1. Structure of an HTML Page

An HTML document contains:

- `<!DOCTYPE html>` → declares the document type.
- `<html>` → root element of the page.
- `<head>` → contains metadata about the page.
- `<body>` → contains visible content displayed on the webpage.

Inside the body:

- `<h3>` tags create headings (e.g., player names).
- `<p>` tags create paragraphs (e.g., salaries).

Data is placed between opening and closing tags.

---

#### 2. Composition of an HTML Tag

Example:

```
<a href="https://www.ibm.com">IBM</a>
```

Components:

- **Tag name:** `a` (anchor tag for hyperlinks)
- **Opening tag:** `<a>`
- **Closing tag:** `</a>`
- **Content:** `IBM`
- **Attribute:** `href`
- **Attribute value:** URL of the webpage

Attributes provide extra information about elements.

---

#### 3. HTML Tree Structure

HTML documents can be represented as a tree:

- Parent tags contain child tags.
- Tags on the same level are siblings.
- Nested tags are descendants.

Example:

- `<html>` is the parent of `<head>` and `<body>`.
- `<title>` is a child of `<head>`.
- `<h1>` and `<p>` inside `<body>` are siblings.

This tree structure helps web scraping tools locate specific elements.

---

#### 4. HTML Tables

Tables are created using:

- `<table>` → defines the table
- `<tr>` → table row
- `<th>` → table header
- `<td>` → table cell

These tags organize data into rows and columns, making tables useful for scraping structured data.

---

### Main Idea

Understanding HTML structure, tags, trees, and tables is essential for web scraping because Python tools use these HTML elements to locate and extract data from webpages.