---
permalink: /terraria-server-status/
---

<!DOCTYPE html>
<html lang="{{ page.lang | default: site.lang | default: 'en' }}">

  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link id="main-stylesheet" rel="stylesheet" href="{{ '/assets/css/style.css' | relative_url }}">
  </head>
  
  <body>
    <main class="page-content" aria-label="Content" >
      <div class="wrapper" >
        <div class="wrapper">
          <div id="status-container">Lade Status...</div>
        </div>
      </div>
    </main>
  </body>

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
        setTimeout(getStatus, 10000);
    }
  
    getStatus();
  </script>

</html>
