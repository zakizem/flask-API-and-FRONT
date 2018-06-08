const infoStore = {
  data: {
    infos: [],
  },
  methods: {
    addInfo(info) {
      infoStore.data.infos.push(info);
    }
  }
};

export default infoStore;
