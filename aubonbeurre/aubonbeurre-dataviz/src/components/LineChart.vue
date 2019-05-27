<script>
import { Line } from 'vue-chartjs'

export default {
  extends: Line,
  props: ["datacollection", "options"],
  data: () => ({
    
  }),
  mounted () {
      console.log(`[LineChartComponent]`, this.chartData, this.options)
      this.renderLineChart()
    
  },
  computed: {
    chartData: function(){
      return this.datacollection
    }
  },
  

  methods: {
    renderLineChart: function() {
      this.renderChart(this.chartData, this.options)
    }
  },

  watch: {
    datacollection: function() {
      this.$data._chart.destroy();
      this.renderLineChart();
    }
  }
}
</script>

<style>
</style>