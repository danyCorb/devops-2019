<script>
  let { APIService } = require('../../api/data.service.js')
  let LineChart = require('../../components/LineChart.vue').default

  module.exports = {
    name: 'data-visualizer-page',
    components: {LineChart},
    props: [],
    data () {
      return {
        selectedUnitNumber: 1,
        selectedAutomateNumber: 1,
        unitNumbers: [1,2,3,4,5],
        automateNumbers: [1,2,3,4,5, 6, 7, 8, 9, 10],
        completeUnitRecording: [],
        datacollections: [],
        items: [
          { message: 'Foo' },
          { message: 'Bar' }
        ],

        chartdata: {
          datacollection: {
            labels: ['January', 'February'],
            datasets: [
              {
                label: 'Data One',
                backgroundColor: '#f87979',
                data: [40, 20]
              }
            ]
          }
        },
        options: {
          responsive: true,
          maintainAspectRatio: false
        },
        myStyles: {
          height: '150px',
          width: '45%',
          position: 'relative'
        }
      }
     
      
    },
    computed: {
      // datacollections: function() {
      //   return this.getAllDataCollections(this.getMockedCompleteUnitRecording(), this.selectedAutomateNumber)
      // },
    },
    mounted () {
      console.log('[DataVisualizerVue] - mounted')

      
      this.getData()
      
    },
    methods: {
      // reload data when user change unit with select element
      onUnitChange(event) {
        console.log(`[DataVisualizerVue] - unit changed ${JSON.stringify(event.target.value)}`)

        this.selectedUnitNumber = Number(event.target.value)
        this.getData()
        
      },
      // change chart data to correspond to the selected automate
      onAutomateChange(event) {
        console.log(`[DataVisualizerVue] - automate changed`)
        
        this.selectedAutomateNumber = Number(event.target.value)
        this.getData()
      },

      // get data from API
      getCompleteUnitRecording(unitNumber) {
        APIService.getInstance().getAutomateRecordsFromUnit(unitNumber).then( data => {
          console.log(`[DataVisualizerVue] - getAutomateRecordsFromUnit - data - ${data}`)
        })
      },

      // get mocked data
      getMockedCompleteUnitRecording() {
        this.completeUnitRecording = [
          {
            number: 1,
            type: 1,
            records: [
              {
                tankTemperature: 1.5,
                externalTemperature: 10.4,
                milkTankWeight: 1.5,
                finalProductWeight: 1.4,
                phMeasurement: 2.3,
                kPosMeasurement: 4,
                naClConcentration: 4.5,
                salmonellaLevel: 1,
                eColiLevel: 1,
                listeriaLevel: 2,
              },
              {
                tankTemperature: 1.6,
                externalTemperature: 8.4,
                milkTankWeight: 1.6,
                finalProductWeight: 1.0,
                phMeasurement: 2.7,
                kPosMeasurement: 3,
                naClConcentration: 4.2,
                salmonellaLevel: 2,
                eColiLevel: 2,
                listeriaLevel: 1,
              }
            ]
          },
          {
            number: 2,
            type: 3,
            records: [
              {
                tankTemperature: 16,
                externalTemperature: 10.4,
                milkTankWeight: 1.5,
                finalProductWeight: 1.4,
                phMeasurement: 2.3,
                kPosMeasurement: 4,
                naClConcentration: 4.5,
                salmonellaLevel: 1,
                eColiLevel: 1,
                listeriaLevel: 2,
              },
              {
                tankTemperature: 1.6,
                externalTemperature: 8.4,
                milkTankWeight: 1.6,
                finalProductWeight: 1.0,
                phMeasurement: 2.7,
                kPosMeasurement: 3,
                naClConcentration: 4.2,
                salmonellaLevel: 2,
                eColiLevel: 2,
                listeriaLevel: 1,
              }
            ]
          }
        ]
      },

      getAllDataCollections(completeUnitRecording, automateNumber) {
        console.log(`[DataVisualizer] - complete unit recording`)
        console.log(completeUnitRecording)

        // Get only data collections for one automate
        const completeAutomateRecord = completeUnitRecording.find( el => el.number === automateNumber)

        console.log(`[DataVisualizer] - complete automate record`)
        console.log(completeAutomateRecord)

        console.log(`Object keys - ${ Object.keys(completeAutomateRecord.records[0])}`)

        // generate the data set for each attribute
        const attributeDataSets = Object.keys(completeAutomateRecord.records[0]).map(key => {
          const data = completeAutomateRecord.records.map(record => record[key])
          const label = key
          const backgroundColor = '#f87979'

          return {label, backgroundColor, data}
        })

        // TO DO : CHANGE WITH RECORD DATE
        const labels = []

        for (let i=1; i <= completeAutomateRecord; i++) {
          labels.push(i.toString())
        }

        const datacollections = attributeDataSets.map(dataset => {
          const datasets = [dataset]
          return {labels, datasets}
        })

        console.log(`[DataVisualizer] - datacollections`)
        console.log(datacollections)

        this.datacollections = datacollections

      },

      getData(){

        // Calculate this every 60 seconds, or every automate or unit change
        // this.getCompleteUnitRecording(this.selectedUnitNumber)
        this.getMockedCompleteUnitRecording()
        // after, get the data collections
        this.getAllDataCollections(this.completeUnitRecording, this.selectedAutomateNumber)
      }

    }
  }
    
</script>

<template>
  <section class="data-visualizer-page">

    <form id="form">
      <!-- Unit select -->
      <label>Unit number</label>
      <select v-model="selectedUnitNumber" @change="onUnitChange($event)">
        <option v-for="unitNumber in unitNumbers" :key="unitNumber">{{unitNumber}}</option>
      </select>

      <!-- Automate select -->
      <label>Automate number</label>
      <select v-model="selectedAutomateNumber" @change="onAutomateChange($event)">
        <option v-for="automateNumber in automateNumbers" :key="automateNumber">{{automateNumber}}</option>
      </select>
    </form>

    <div id="line-charts-container">
      <LineChart 
        :styles="myStyles"
        v-for="(datacollection, i) in this.datacollections"
        class="small"
        :datacollection=datacollection
        :options=options
        v-bind:key="i"
      >
      </LineChart>
    </div>
    
    

  </section>
</template>

<style>
  .data-visualizer-page {
    
  }

  #form {
    display: flex;
    background-color:mediumseagreen;
    color: white;
    padding: 20px;
    justify-content: center;
    align-items: center;

  }

  #form select {
    margin: 0 20px;
  }

  .small {
    position:relative
  }

  .chartjs-render-monitor {
    
  }

  #line-charts-container {
    width: 100%;
    display: flex;
    flex-wrap: wrap;
    flex-direction: row;
    justify-content: space-around;
  }
</style>