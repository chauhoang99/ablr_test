const template = `
<div v-show="isActive"><slot></slot></div>
`

export default {
    template,
        props: {
        name: { required: true },
        selected: { default: false}
    },

    data() {

        return {
            isActive: false
        };

    },

    computed: {

        href() {
            return '#' + this.name.toLowerCase().replace(/ /g, '-');
        }
    },

    mounted() {

        this.isActive = this.selected;

    }
}