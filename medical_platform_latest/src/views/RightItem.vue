<template>
    <div class="containerr">
        <img class="headr" src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png" />
        <div class="contentr">
            <div class="textr" v-if="type === 0" style="word-break: break-all;">
                {{ content }}
            </div>
        </div>
    </div>
</template>
<script></script>
<script>

    export default {
        name: "RightItem",
        props: ['id', 'type', 'content']
    }
</script>

<style>
.containerr {
    display: flex;
    /* padding: 10px 15px;
    margin-left: 60px; */
    flex-direction: row-reverse;
}

.headr {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    border: 1px solid #eee;
}

.contentr {
    margin-right: 10px;
    margin-top: 10px;
}

.textr {
    background-color: #eee;
    border-bottom-left-radius: 10px;
    padding: 5px 5px;
    font-size: 14px;
    color: #000;
    float:right;
}
</style>
