<template>
    <div class="containerl">
        <img class="headl" src="https://pp.myapp.com/ma_icon/0/icon_42284557_1517984341/96"/>
        <div class="contentl">
            <div class="textl" v-if="type === 1">
                {{content}}
            </div>
        </div>
    </div>
</template>

<script>
export default {
  name: 'LeftItem',
  props: ['id', 'type', 'content']
}
</script>

<style >
    .containerl {
        display: flex;
        /* padding: 10px 15px;
        margin-right: 60px; */
        /* flex-direction: row-reverse; */
    }
    .headl {
        width: 40px;
        height: 40px;
        border-radius: 50%;
        border: 1px solid #eee;
    }

    .contentl {
        margin-left: 10px;
        margin-top: 10px;
    }
    .textl {
        background-color: deepskyblue;
        border-bottom-right-radius: 10px;
        padding: 5px 5px;
        font-size: 14px;
        color: #fff;
        /* float:right; */
        float:left;
    }

</style>
