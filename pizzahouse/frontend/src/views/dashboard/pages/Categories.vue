<template>
  <v-container id="categorie" fluid tag="section">
    <v-data-table
    :headers="headers"
    :items="categories"
    class="elevation-1"
  >
    <template v-slot:top>
      <v-toolbar
        flat
      >
        <v-toolbar-title>Catégories</v-toolbar-title>
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
                      v-model="editedItem.category_name"
                      label="Nom Catégorie"
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
            <v-card-title class="headline">Etes vous sur de vouloir supprimer cette catégorie?</v-card-title>
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
  name: 'categorie',
  data: () => ({
      dialog: false,
      dialogDelete: false,
      headers: [
        {
          text: 'category_id',
          value: 'category_id'
        },
        { text: 'category_name', value: 'category_name'},
        { text: 'Actions', value: 'actions'},
      ],
      categories: [],
      editedIndex: -1,
      editedItem: {
        category_id: '',
        category_name: '',
      },
      defaultItem: {
        category_id: '',
        category_name: '',
      },
    }),

    computed: {
      formTitle () {
        return this.editedIndex === -1 ? 'Nouvelle Catégorie' : 'Modifier Catégorie'
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
      axios.get('http://127.0.0.1:8000/api/categories/').then((response) => {
        this.categories = response.data;
      });
    },
      editItem (item) {
        this.editedIndex = this.categories.indexOf(item)
        this.editedItem = Object.assign({}, item)
        this.dialog = true;
        axios.put('http://127.0.0.1:8000/api/categories/'+item.category_id+'/')
          .then(response => {
            console.log("id:"+item.category_id);
            console.log(response);
    })
      },

      deleteItem (item) {
        console.log(item);
        this.editedIndex = this.categories.indexOf(item)
        this.editedItem = Object.assign({}, item)
        this.dialogDelete = true
        console.log('deleted data');
        axios.delete('http://127.0.0.1:8000/api/categories/'+item.category_id)
            .then(response=>{
              console.log(response);
            })
      },

      deleteItemConfirm () {
        this.categories.splice(this.editedIndex, 1)
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
          console.log('edited data');
          console.log(this.editedItem);
          axios.put('http://127.0.0.1:8000/api/categories/'+this.editedItem.category_id+'/',{
            category_name: this.editedItem.category_name})
            .then(response=>{
              console.log('response:'+response);
            })
          Object.assign(this.categories[this.editedIndex], this.editedItem)
        } else {
          axios.post('http://127.0.0.1:8000/api/categories/',{category_id: this.editedItem.category_id, category_name: this.editedItem.category_name})
           .then(function (response) {
              console.log(response);
          })
           .catch(function (error) {
              console.log(error);
          });
          this.categories.push(this.editedItem)
          console.log('created data');
        }
        this.close()
      },
    },
}
</script>
