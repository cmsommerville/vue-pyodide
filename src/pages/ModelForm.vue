<template>
  <div class="container">
    <h1>Iris Classifier</h1>
    <form @submit.prevent="executePython">
      <div
        class="input-wrapper"
        v-for="(param, index) in modelParams"
        :key="param.id"
      >
        <label class="label" :for="param.id">{{ param.name }}</label>
        <input
          class="input"
          :type="param.inputType"
          :id="param.id"
          v-model="modelParams[index].val"
        />
      </div>
      <div class="d-flex justify-content-center" v-if="!pyodideLoaded">
        <div class="spinner-border" role="status">
          <span class="visually-hidden">Loading...</span>
        </div>
      </div>
      <button class="btn" id="btn-score-model" v-if="pyodideLoaded">
        <div class="btn-loaded">
          Score Model
        </div>
      </button>
    </form>

    <transition name="slide-fade">
      <div class="iris" v-if="iris">
        <h4>
          The iris species is: <span class="iris-species">{{ iris }}</span
          >.
        </h4>
      </div>
    </transition>
    <div>
      <p v-if="errorMsg">{{ errorMsg }}</p>
    </div>
  </div>
</template>

<script>
import modelConfig from "../python/model";

export default {
  name: "ModelForm",
  data() {
    return {
      pyodideLoaded: false,
      errorMsg: "",
      iris: null,
      modelParams: modelConfig.modelInputs,
    };
  },
  async mounted() {
    this.initializePyodide();
  },
  computed: {
    paramList() {
      return this.modelParams.map((param) => param.val);
    },
  },
  methods: {
    async initializePyodide() {
      try {
        window.languagePluginUrl =
          "https://cdn.jsdelivr.net/pyodide/v0.17.0/full/";
        await this.$loadScript(
          "https://cdn.jsdelivr.net/pyodide/v0.17.0/full/pyodide.js"
        );
        // wait for pyodide ready
        await window.languagePluginLoader;
        await window.pyodide.loadPackage(modelConfig.packages);
        await window.pyodide.runPythonAsync(modelConfig.imports);

        this.pyodideLoaded = true;
        this.$emit("pyodide-loaded");
      } catch (error) {
        this.errorMsg = error;
      }
    },
    async executePython() {
      this.iris = null;
      await window.pyodideReadyPromise;
      try {
        this.iris = await modelConfig.scoreModel(
          modelConfig.model,
          this.paramList
        );
      } catch (err) {
        this.errorMsg = err.message;
      }
    },
  },
};
</script>

<style>
form,
.iris {
  border: 1px solid #ddd;
  border-radius: 2px;
  width: 50%;
  margin: 1rem auto;
  padding: 1rem;
}

.label {
  display: block;
}

.input-wrapper {
  margin-bottom: 1rem;
}

.iris-species {
  font-style: italic;
}

#btn-score-model {
  background-color: hsl(105, 50%, 85%);
  color: #222;
  transition: all 0.2s ease-out;
}

#btn-score-model:hover {
  background-color: hsl(105, 70%, 70%);
  transform: scale(1.05);
}
</style>
