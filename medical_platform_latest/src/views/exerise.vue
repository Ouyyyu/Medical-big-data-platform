<template>
<div>
<div class="box_x">
    <div class="title">
        <div class="cat1"><img src="../assets/3.png" class="cat1"/><img src="../assets/3.png" class="cat1"/><img src="../assets/3.png" class="cat1"/><img src="../assets/3.png" class="cat1"/><img src="../assets/3.png" class="cat1"/></div>
        <!-- <img src="../assets/跨栏跑步.png"/> -->
    <div class="box1"><h1 class="title4">运动小贴士</h1></div>
    <div class="cat2"><img src="../assets/10.png" class="cat2"/><img src="../assets/10.png" class="cat2"/><img src="../assets/10.png" class="cat2"/><img src="../assets/10.png" class="cat2"/><img src="../assets/10.png" class="cat2"/></div>
</div>
<!-- <div class="right">
    <img src="../assets/YaHong.png"/>

</div> -->
<!-- <div class="tupianbottom"><img src="../assets/女_奔跑.svg.png"/>></div> -->
    <h2>运动后不要大量喝水</h2>
    <div class="content">在运动量加大时，消耗的能量增加，心跳和呼吸的次数都会有明显的加快。此时，大量带有氧气的血液流向四肢和体表，供肌肉活动的需要。胃肠道的血液量就相对减少了，对水的吸收能力也相应降低。如果运动后即喝很多水，胃内的水分不能及时送到小肠进行吸收和利用，水就贮留在胃里，会感到不适。而且胃内水分多过，胃酸被冲淡，减弱了杀菌和消化的能力。
更不能饮用凉水，会使喉咙、食管、胃等器官遇冷而急剧收缩，使人感到不适。这就是俗话所说的“炸肺”。</div>
<h2>运动后不能急喝冷饮</h2>
<div class="content">剧烈运动能使体温上升到39℃左右,这时大量吃冷饮对消化道是一个强冷刺激,会引起消化道强烈蠕动,产生腹痛、腹泻。同时,冷热的急剧变化会使胃部血管突然收缩,次数多了就会引起消化吸收功能失调.</div>
<h2>运动后不能吃大量高脂高蛋白食物</h2>
<div class="content">这些食品不但不利于解除疲劳,反而增加胃部和身体的负担，反而感觉肌肉发胀、关节酸痛、精神疲乏加重。应该食用碱性食物，比如豆类及豆制品；菠菜、莴笋、萝卜、土豆、藕、洋葱、海带、苹果等瓜果蔬菜海菜类；牛奶及奶制品类等。</div>
<h2>剧烈运动后少吃甜食</h2>
<div class="content">运动后过多吃甜食会使体内的维生素B1大量消耗，使人感到倦怠、食欲不振等，影响体力的恢复。</div>
<h2>运动后不能马上洗澡</h2>
<div class="content">运动时由于肌肉要用劲，流向肌肉的血液增加，心率加快。运动停止后， 血液的流动和加快的心率虽有所缓解，但仍会持续一段时间。如果这时立即洗热水澡，血液往肌肉和皮肤的流量会继续大量增加，剩余的血液可能不足 以供应身体其它器官的需要，尤其是心脏和脑部的需要，以致心脏病突发或 脑部缺氧。</div>
<h2>运动后半小时不能吃东西</h2>
<div class="content">运动后不要马上进食，因为运动时血液集中在肌肉，吃饭会使血液流向胃部，会影响心脏功能，对胃也不好；运动以后人的吸收特别好，很容易长胖。</div>
<h2>运动后为什么不能喝酒</h2>
<div class="content">运动中情绪激动,呼吸加深、心跳加速，喝酒的不良刺激加剧了这种生理反应。</div>
<h2>空腹或剧烈运动后不能游泳</h2>
<div class="content">剧烈运动后不能立刻下水，易引起低血糖而昏倒。</div>
<h2>运动后不能立即睡觉</h2>
<div class="content">运动使肌肉紧张，神经兴奋，容易失眠。</div>
<a href="#/health" class="huidao1">下一篇</a>
<a href="/home" class="huidao">回到首页</a>
<!-- <el-button type="success" class="huidao" @click="make">回到首页</el-button> -->
</div>
</div>

</template>
<script></script>
<!-- <script>
    export default {
        name:"exerise",
        methods:{
            make() {
                this.$router.push("./home");
            }
        }
    }
</script> -->
<style>
.huidao1 {
    text-decoration: none;
}
.huidao {
    margin-left: 1250px;
    font-size: 25px;
    color:#FF88C2;
    text-decoration: none;
    position: fixed;
    bottom :0;
}
.huidao:hover {
    text-decoration: none;
    color:aquamarine;
}
.box1 {
    background-color: rgba(215, 236, 250, 0.769);
    width:400px;
    margin:0 auto;
    border-top-left-radius:50px;
    border-top-right-radius:50px;
    box-shadow: 5px 5px 3px 4px rgb(215, 236, 250);
}
.title4{
    color:transparent;
    -webkit-text-stroke:1px #FF88C2;
     letter-spacing: 0.04em;
     /* display:inline-block;
    float:left;
    margin-left:250px; */
}
/* .cat1 {
    display:inline-block;
    float:left;
    margin-left:200px;
}
.cat2 {
    display:inline-block;
    float:left;
    margin-left:300px;
} */
.box_x{

background:url("../assets/女_奔跑.svg.png") left bottom ,url("../assets/人物6-运动的人2.png") right top;
/* background-position: left bottom; */
background-repeat :no-repeat;
background-attachment:fixed;
background-size: 500px, 300px;
}
/* .right {
    width:20px;
    position: absolute;
    margin-right: 0px;
    margin-bottom: 0px;
} */
/* .tupianbottom {
    margin-left: 0px;
    margin-bottom: 0px;
    width: 150px;
    position:absolute;
} */
.tupian1 {
    height:100px;
    /* margin-left: 50px; */
}
.content {
    margin-left:350px;
    margin-right:350px;
    font-size:18px;
    line-height: 2em;
}
.box {
    /* background-image: url("../assets/跨栏跑步.png") ; */
    /* text-align: center; */
    /* background-color: rgb(215, 250, 247); */
}
.title {
    color:rgb(0, 166, 255);
    font: 12px/1.5 Tahoma,Helvetica,Arial,‘宋体’,sans-serif;
    font-weight: 800;
    text-align: center;
    font-size: 30px;
}
.box_x h2 {
    text-align: center;
    color:rgb(250, 221, 215);
}
</style>
