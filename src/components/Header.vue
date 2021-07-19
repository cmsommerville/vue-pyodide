<template>
  <header>
    <nav>
      <div class="progress-bar" v-if="loading"></div>
      <div class="nav-logo">
        <img src="@/assets/logo.png" alt="Company logo" class="logo-image" />
      </div>
      <div class="nav-title">
        <h2>Actuarial Pricing</h2>
      </div>
    </nav>
  </header>
</template>

<script>
export default {
  name: "Header",
  props: {
    loading: {
      type: Boolean,
      default: false,
    },
  },
};
</script>

<style>
.logo-image {
  width: 50px;
  height: 50px;
}

header {
  position: sticky;
  top: 0;
  left: 0;
  font-family: Avenir, Helvetica, Arial, sans-serif;
}

nav {
  background-color: hsl(153, 50%, 75%);
  height: 70px;
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-direction: row;
}

.nav-logo,
.nav-title {
  padding: 10px 20px;
  z-index: 2;
}

.progress-bar {
  position: absolute;
  width: calc(100% * 3 / 7);
  height: 100%;
  display: flex;
  animation: move 2s linear infinite;
  background-image: linear-gradient(
    to right,
    hsl(153, 50%, 75%),
    hsl(153, 65%, 60%) 50%,
    hsl(153, 50%, 75%) 100%
  );
}

@keyframes move {
  0% {
    transform: translate(-100%, 0);
  }
  100% {
    transform: translate(calc(7 / 3 * 100%), 0);
  }
}
</style>
