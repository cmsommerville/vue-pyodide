<template>
  <div id="app2">
    <Header :loading="pyodideLoading" />
    <transition name="slide-fade" appear>
      <div id="app">
        <ModelForm @pyodide-loaded="handlePyodideLoaded" />
      </div>
    </transition>
  </div>
</template>

<script>
import ModelForm from "./pages/ModelForm.vue";
import Header from "./components/Header.vue";

export default {
  name: "App",
  components: {
    ModelForm,
    Header,
  },
  data() {
    return {
      pyodideLoading: true,
    };
  },
  methods: {
    handlePyodideLoaded() {
      this.pyodideLoading = false;
    },
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.slide-fade-enter-active,
.slide-fade-leave-active {
  transition: all 0.5s ease;
}

.slide-fade-enter,
.slide-fade-leave-to {
  transform: translateY(20px);
  opacity: 0;
}
</style>
