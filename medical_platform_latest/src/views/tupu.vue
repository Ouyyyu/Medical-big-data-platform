<template>
  <div class="neo4jMain">
    <el-row :gutter="5">
        <el-col :span="4">
          <img class="img1" src="../assets/ourlogo.png" height=90px width=250px style="margin:5px;">
        </el-col>
        <el-col :span="8" class="menu">
          <div sytle="display: table-cell;margin: 0 auto;">
            <el-menu :default-active="activeIndex" mode="horizontal" text-color="#409eff">
              <el-menu-item index="1"><a href="#/home"
                  style="font-size: 20px; text-align: center; text-decoration: none;">首页</a>
              </el-menu-item>
              <el-menu-item index="2"><a href="#/baike"
                  style="font-size: 20px; text-align: center; text-decoration: none;">医疗百科</a>
              </el-menu-item>
              <el-menu-item index="3"><a href="#/person"
                  style="font-size: 20px; text-align: center; text-decoration: none;">个人档案</a>
              </el-menu-item>
              <el-menu-item index="4"><a href="#/chat"
                  style="font-size: 20px; text-align: center; text-decoration: none; ">医疗问诊</a>
              </el-menu-item>
            </el-menu>
          </div>
        </el-col>
        <el-col :span="12"></el-col>
      </el-row>

    <div class="echarts" ref="echarts" style="width: 1500px;height:600px;">
    </div>
  </div>
</template>
<script></script>
<script>
import * as echarts from 'echarts'

export default {
  name: "tupu",
  mounted() {
    var getcookie=this.$cookies.get("disease");
    // alert(getcookie)
    if(getcookie !== null){
      this.disease = getcookie;
      this.onSubmit();
    }
    else{
      this.query();
    }
  },
  data() {
    return {
      formInline: {
        startNode: '',
        endNode: '',
        relationName: ''
      },
      rules: {
        startNode: [{ required: true, trigger: 'blur' }],
        endNode: [{ required: true, trigger: 'blur' }],
        relationName: [{ required: true, trigger: 'blur' }]
      },
      protocol: 'bolt',
      host: '43.142.181.243',
      port: 7687,
      username: 'neo4j',
      password: '123456',
      echartsData: [],
      nodesRelation: []
    }
  },
  methods: {
    initEcharts() {
      // 基于准备好的dom，初始化echarts实例
      let myChart = echarts.init(this.$refs.echarts)
      // 绘制图表
      myChart.setOption({
        title: {
          text: '医疗百科 图谱关系'
        },
        tooltip: {},
        animationDurationUpdate: 1500,
        animationEasingUpdate: 'quinticInOut',
        series: [
          {
            type: 'graph',
            layout: 'force',
            force: {
              edgeLength: 40,
              repulsion: 50,
              gravity: 0.1
            },
            symbolSize: 50,
            roam: true,
            label: {
              show: true
            },
            edgeSymbol: ['circle', 'arrow'],
            edgeSymbolSize: [4, 10],
            edgeLabel: {
              fontSize: 20
            },
            data: this.echartsData,
            // links: [],
            links: this.nodesRelation,
            lineStyle: {
              opacity: 0.9,
              width: 2,
              curveness: 0
            }
          }
        ]
      });
    },
    query() {
      this.connect();
      const session = this.$neo4j.getSession();
      let cypher = `MATCH (n) RETURN n LIMIT 40`;

      session.run(cypher).then(res => {
        let records = res.records;
        let nodes = new Set();
        this.nodesRelation = [];
        for (let i = 0; i < records.length; i++) {
          nodes.add(records[i]._fields[0].properties.name);
          nodes.add(records[i]._fields[0].properties.cure_department[0]);
          nodes.add(records[i]._fields[0].properties.cure_way[0]);

          this.nodesRelation.push({
            source: records[i]._fields[0].properties.name,
            target: records[i]._fields[0].properties.cure_department[0],
            lineStyle: {
              curveness: 0
            },
            label: {
              show: true,
              formatter: function () {
                return ''
              }
            }
          });
        }
        let curveness = [0, 0.4, -0.4, 0.3, -0.3, 0.2, -0.2, 0.1, -0.1];
        for (let j = 0; j < this.nodesRelation.length; j++) {
          let repeatNumber = 0;
          for (let s = j + 1; s < this.nodesRelation.length; s++) {
            let r1 = this.nodesRelation[j];
            let r2 = this.nodesRelation[s];
            if (r1.source === r2.source &&
              r1.target === r2.target) {
              repeatNumber = repeatNumber + 1;
            }
            else if (r1.target === r2.source &&
              r1.source === r2.target) {
              repeatNumber = repeatNumber + 1;
            }
          }
          this.nodesRelation[j].repeatNumber = repeatNumber;
        }
        for (let j = 0; j < this.nodesRelation.length; j++) {
          // console.log(this.nodesRelation[j].repeatNumber);
          this.nodesRelation[j].lineStyle.curveness = curveness[this.nodesRelation[j].repeatNumber];
        }

        this.echartsData = [];
        nodes.forEach((e) => {
          let index = Math.ceil(Math.random() * 10);
          let color = () => {
            if (index % 4 === 0) {
              return '#228B22'
            } else if (index % 4 === 1) {
              return '#FFFF00'
            } else if (index % 4 === 2) {
              return '#20B2AA'
            } else if (index % 4 === 3) {
              return '#FFB6C1'
            }
            return '#87CEFA';
          }
          this.echartsData.push({
            name: e,
            x: Math.random() * 100,
            y: Math.random() * 100,
            itemStyle: {
              color: color()
            }
          });
        })
        this.initEcharts();
      }).then(() => {
        session.close()
      });
    },
    onSubmit() {
      this.connect();
      const session = this.$neo4j.getSession();
      // this.aaa = '放射性肺炎'
      let cypher = `match (n:Disease)where n.name="${this.disease}" return n`;
      session.run(cypher).then(res => {
        let records = res.records;
        console.log(records);
        let nodes = new Set();
        this.nodesRelation = [];
        nodes.add(records[0]._fields[0].properties.name);
        nodes.add(records[0]._fields[0].properties.cure_department[0]);
        nodes.add(records[0]._fields[0].properties.cure_way[0]);
        nodes.add(records[0]._fields[0].properties.cure_lasttime);
        nodes.add(records[0]._fields[0].properties.easy_get);
        nodes.add(records[0]._fields[0].properties.cured_prob);
        // nodes.add(records[0]._fields[0].properties.cause);
        // nodes.add(records[0]._fields[0].properties.prevent);

        this.nodesRelation.push({
          source: records[0]._fields[0].properties.name,
          target: records[0]._fields[0].properties.cure_department[0],
          lineStyle: {
            curveness: 0
          },
          label: {
            show: true,
            formatter: function () {
              return '属于'
            }
          }
        });
        this.nodesRelation.push({
          source: records[0]._fields[0].properties.name,
          target: records[0]._fields[0].properties.cure_way[0],
          lineStyle: {
            curveness: 0
          },
          label: {
            show: true,
            formatter: function () {
              return '治疗方式'
            }
          }
        });
        this.nodesRelation.push({
          source: records[0]._fields[0].properties.name,
          target: records[0]._fields[0].properties.cure_lasttime,
          lineStyle: {
            curveness: 0
          },
          label: {
            show: true,
            formatter: function () {
              return '治疗时间'
            }
          }
        });
        this.nodesRelation.push({
          source: records[0]._fields[0].properties.name,
          target: records[0]._fields[0].properties.easy_get,
          lineStyle: {
            curveness: 0
          },
          label: {
            show: true,
            formatter: function () {
              return '易感人群'
            }
          }
        });
        this.nodesRelation.push({
          source: records[0]._fields[0].properties.name,
          target: records[0]._fields[0].properties.cured_prob,
          lineStyle: {
            curveness: 0
          },
          label: {
            show: true,
            formatter: function () {
              return '治愈概率'
            }
          }
        });

        let curveness = [0, 0.4, -0.4, 0.3, -0.3, 0.2, -0.2, 0.1, -0.1];
        for (let j = 0; j < this.nodesRelation.length; j++) {
          let repeatNumber = 0;
          for (let s = j + 1; s < this.nodesRelation.length; s++) {
            let r1 = this.nodesRelation[j];
            let r2 = this.nodesRelation[s];
            if (r1.source === r2.source &&
              r1.target === r2.target) {
              repeatNumber = repeatNumber + 1;
            }
            else if (r1.target === r2.source &&
              r1.source === r2.target) {
              repeatNumber = repeatNumber + 1;
            }
          }
          this.nodesRelation[j].repeatNumber = repeatNumber;
        }
        for (let j = 0; j < this.nodesRelation.length; j++) {
          // console.log(this.nodesRelation[j].repeatNumber);
          this.nodesRelation[j].lineStyle.curveness = curveness[this.nodesRelation[j].repeatNumber];
        }

        this.echartsData = [];
        nodes.forEach((e) => {
          let index = Math.ceil(Math.random() * 10);
          let color = () => {
            if (index % 4 === 0) {
              return '#228B22'
            } else if (index % 4 === 1) {
              return '#FFFF00'
            } else if (index % 4 === 2) {
              return '#20B2AA'
            } else if (index % 4 === 3) {
              return '#FFB6C1'
            }
            return '#87CEFA';
          }
          this.echartsData.push({
            name: e,
            x: Math.random() * 100,
            y: Math.random() * 100,
            itemStyle: {
              color: color()
            }
          });
        })
        this.initEcharts();
      }).then(() => {
        session.close()
      });
    },
    connect() {
      return this.$neo4j.connect(this.protocol, this.host, this.port, this.username, this.password);
    }

  }
}
</script>

<style>
  .menu {
  margin: 20px;
}

.img1 {
  margin-top: -10px;
}
.neo4jMain {
  height: 100%;
  display: flex;
  flex-direction: column;

}
.echarts {
    background-color: aliceblue;
    flex: 1;
    flex-grow: 1;
  }
</style>
