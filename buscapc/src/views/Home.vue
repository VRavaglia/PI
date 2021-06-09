<template>
  <div class="home">
    <p class="has-text-centered"><big>
      {{ this.foo2 }}
    </big></p>
  </div>
</template>

<script>

export default {
  data() {
    return{
      foo2: this.foo
    }
  },

  name: 'Home',
  components: {
    
  }
}
</script>
