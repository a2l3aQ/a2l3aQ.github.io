---
permalink: /terraria-server-status/
layout: nohead
---
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
