import Header from './header/header.js'
import Content from './content/content.js'
import Footer from './footer/footer.js'
import Result from './result/result.js'

const App = {
  el: 'main',

  components: {
    'app-header': Header,
    'app-content': Content,
    'app-footer': Footer,
    'app-result': Result
  }
}


window.addEventListener('load', () => {
  new Vue(App)
})
