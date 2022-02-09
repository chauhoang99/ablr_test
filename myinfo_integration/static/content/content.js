const template = `
  <section>

    <label>
      {{ message }}
    </label>

    <div>
      <button @click="click()">Retrieve My Info</button>
    </div>

  </section>
`

export default {
  template,

  data () {
    return {
      message: 'This is just a demo. Please click Retrieve My Info to start.'
    }
  },

  methods: {
    click () {
      window.open("/auth", "_self");
    }
  }
}
