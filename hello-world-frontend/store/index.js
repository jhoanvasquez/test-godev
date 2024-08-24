export const state = () => ({
  content: ''
});

export const mutations = {
  updateContent(state, newContent) {
    state.content = newContent;
  },
  updateData(state, newData) {
    state.content = newData;
  }
};