<template>
  <div class="container">
    <iframe id="tempHtml" ref="tempHtml" frameborder="0" width="100%" height="100%"
      src='http://localhost:8081/'></iframe>
      <a href="/home">回到首页</a>
  </div>
</template>

<style>
* {
  margin: 0;
  padding: 0;
}
a {
  color:cornflowerblue;
  text-decoration: none;
}
a:hover {
  text-decoration: none;
  color:blueviolet;
}
.container {
  width: 100%;
  /* height: auto; */
  height: 1280px;
}
</style>
