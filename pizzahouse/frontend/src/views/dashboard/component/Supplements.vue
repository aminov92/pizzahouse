<template>
  <v-container id="supplement" fluid tag="section">
    <v-data-table
    :headers="headers"
    :items="Supplements"
    class="elevation-1"
  >
    <template v-slot:top>
      <v-toolbar
        flat
      >
        <v-toolbar-title>Supplements</v-toolbar-title>
        <v-divider
          class="mx-4"
          inset
          vertical
        ></v-divider>
        <v-spacer></v-spacer>
        <v-dialog
          v-model="dialog"
          max-width="500px"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-btn
              color="primary"
              dark
              class="mb-2"
              v-bind="attrs"
              v-on="on"
            >
              Ajouter 
            </v-btn>
          </template>
          <v-card>
            <v-card-title>
              <span class="headline">{{ formTitle }}</span>
            </v-card-title>

            <v-card-text>
              <v-container>
                <v-row>
                  <v-col>
                    <v-text-field
                      v-model="editedItem.supplement_name"
                      label="Nom supplément"
                    ></v-text-field>
                  </v-col>
                </v-row>
              </v-container>
            </v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn
                color="blue darken-1"
                text
                @click="close"
              >
                Annuler
              </v-btn>
              <v-btn
                color="blue darken-1"
                text
                @click="save"
              >
                Sauvegarder
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
        <v-dialog v-model="dialogDelete" max-width="500px">
          <v-card>
            <v-card-title class="headline">Etes vous sur de vouloir supprimer ce supplément?</v-card-title>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" text @click="closeDelete">Annuler</v-btn>
              <v-btn color="blue darken-1" text @click="deleteItemConfirm">OK</v-btn>
              <v-spacer></v-spacer>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-toolbar>
    </template>
    <template v-slot:[`item.actions`]="{ item }">
      <v-icon
        small
        class="mr-2"
        @click="editItem(item)"
      >
        mdi-pencil
      </v-icon>
      <v-icon
        small
        @click="deleteItem(item)"
      >
        mdi-delete
      </v-icon>
    </template>
    <template v-slot:no-data>
      <v-btn
        color="primary"
        @click="initialize"
      >
        Reset
      </v-btn>
    </template>
  </v-data-table>
  </v-container>
</template>
<script>
  import axios from 'axios';
  export default {
  name: 'supplement',
  data: () => ({
      dialog: false,
      dialogDelete: false,
      headers: [
        {
          text: 'supplement_id',
          value: 'supplement_id'
        },
        { text: 'supplement_name', value: 'supplement_name'},
        { text: 'Actions', value: 'actions'},
      ],
      Supplements: [],
      editedIndex: -1,
      editedItem: {
        supplement_id: '',
        supplement_name: '',
      },
      defaultItem: {
        supplement_id: '',
        supplement_name: '',
      },
    }),

    computed: {
      formTitle () {
        return this.editedIndex === -1 ? 'Nouveau supplément' : 'Modifier supplément'
      },
    },

    watch: {
      dialog (val) {
        val || this.close()
      },
      dialogDelete (val) {
        val || this.closeDelete()
      },
    },

    created () {
      this.getItem();
    },

    methods: {
      getItem() {
      axios.get('http://127.0.0.1:8000/api/supplements/').then((response) => {
        this.Supplements= response.data;
      });
    },
      editItem (item) {
        this.editedIndex = this.Supplements.indexOf(item)
        this.editedItem = Object.assign({}, item)
        this.dialog = true;
        axios.put('http://127.0.0.1:8000/api/supplements/'+item.supplement_id+'/')
          .then(response => {
            console.log(response);
    })
      },

      deleteItem (item) {
        console.log(item);
        this.editedIndex = this.Supplements.indexOf(item)
        this.editedItem = Object.assign({}, item)
        this.dialogDelete = true
        axios.delete('http://127.0.0.1:8000/api/supplements/'+item.supplement_id)
            .then(response=>{
              console.log(response);
            })
      },

      deleteItemConfirm () {
        this.Supplements.splice(this.editedIndex, 1)
        this.closeDelete()
      },

      close () {
        this.dialog = false
        this.$nextTick(() => {
          this.editedItem = Object.assign({}, this.defaultItem)
          this.editedIndex = -1
        })
      },

      closeDelete () {
        this.dialogDelete = false
        this.$nextTick(() => {
          this.editedItem = Object.assign({}, this.defaultItem)
          this.editedIndex = -1
        })
      },

      save () {
        if (this.editedIndex > -1) {
          console.log(this.editedItem);
          axios.put('http://127.0.0.1:8000/api/supplements/'+this.editedItem.supplement_id+'/',{
            supplement_name: this.editedItem.supplement_name})
            .then(response=>{
              console.log('response:'+response);
            })
          Object.assign(this.Supplements[this.editedIndex], this.editedItem)
        } else {
          axios.post('http://127.0.0.1:8000/api/supplements/',{supplement_id: this.editedItem.supplement_id, supplement_name: this.editedItem.supplement_name})
           .then(function (response) {
              console.log(response);
          })
           .catch(function (error) {
              console.log(error);
          });
          this.Supplements.push(this.editedItem)
        }
        this.close()
      },
    },
}
</script>
