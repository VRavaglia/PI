<template>
  <div id="wrapper">
    <nav class="navbar is-dark">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item"><strong>BuscaPC</strong></router-link>
      </div>

    <div class="navbar-menu" id="navbar-menu">
      <div class="navbar-end">
        <router-link to="/mobo" class="navbar-item">Placa Mae</router-link>
        <router-link to="/cpu" class="navbar-item">CPU</router-link>
        <router-link to="/gpu" class="navbar-item">GPU</router-link>
        <router-link to="/case" class="navbar-item">Case</router-link>
        <router-link to="/ram" class="navbar-item">RAM</router-link>
        <router-link to="/fonte" class="navbar-item">Fonte</router-link>
        <router-link to="/armazenamento" class="navbar-item">Armazenamento</router-link>
        
        <div class="navbar-item">
          <div class="buttons">
            <router-link to="/lista" class="button is-light">Lista de Peças</router-link>
          </div>
        </div>

      </div>
    </div>
    </nav>
  </div>
  <section class="section">
    <router-view/>
  </section>

  <footer class="footer">
    <p class="has-text-centered"> Projeto Integrado - UFRJ 2021</p>
  </footer>
   
</template>

<style lang="scss">
@import '../node_modules/bulma';
</style>
