---
permalink: /terraria-server-status/
---

<!DOCTYPE html>
<html style="background-color:rgba(0, 0, 0, 0.3);" lang="{{ page.lang | default: site.lang | default: 'en' }}">

  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    {%- seo -%}
    <link id="main-stylesheet" rel="stylesheet" href="{{ '/assets/css/style.css' | relative_url }}">
    {%- feed_meta -%}
    {%- if jekyll.environment == 'production' and site.google_analytics -%}
      {%- include google-analytics.html -%}
    {%- endif -%}
  
    {%- include custom-head.html -%}
    
  </head>
  
  <body style="background-color:rgba(0, 0, 0, 0.0);">

    <main class="page-content" aria-label="Content" style="background-color:rgba(0, 0, 0, 0.0);">
      <div class="wrapper" style="background-color:rgba(0, 0, 0, 0.0);">
        <div class="wrapper">
          <div id="status-container">Lade Status...</div>
          <script>
              const url = 'https://raw.githubusercontent.com/a2l3aQ/a2l3aQ.github.io/refs/heads/master/terraria_server_status';
              const container = document.getElementById('status-container');
          
              async function getStatus() {
                  try {
                      const response = await fetch(url, {cache: "no-store"});
                      
                      if (!response.ok) {
                          throw new Error('Netzwerk-Antwort war nicht ok');
                      }
          
                      const data = await response.text();
                      container.textContent = data;
                  } catch (error) {
                      container.textContent = 'Fehler beim Laden: ' + error.message;
                      console.error('Da lief was schief:', error);
                  }
              }
          
              getStatus();
          </script>
        </div>
      </div>
    </main>

  </body>

</html>
