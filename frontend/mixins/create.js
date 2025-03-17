import { reactive } from 'vue'

export const create = reactive({
  createDialog: true,
  show () {
    this.createDialog = true
  },
  hide () {
    this.createDialog = false
  },
  toggle () {
    this.createDialog = !this.createDialog
  }
})