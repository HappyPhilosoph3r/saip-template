<script setup lang="ts">

  const glossary = [
    {
      name: 'Test',
      description: "A metric for analysing performance or ensuring that a function performs correctly",
    },
    {
      name: '411',
      description: "A set or information or details about an item or concept. Example: 'What is the 411 on the " +
          "weather today?'",
    },
    {
      name: 'awc',
      description: "An abbreviation for 'anyone who cares' ",
    }
  ]

</script>
<template>
  <h1> Glossary </h1>
  <v-table>
    <thead>
    <tr>
      <th class="text-left">
        Name
      </th>
      <th class="text-left">
        Description
      </th>
    </tr>
    </thead>
    <tbody>
    <tr
        v-for="item in glossary"
        :key="item.name"
    >
      <td>{{ item.name }}</td>
      <td>{{ item.description }}</td>
    </tr>
    </tbody>
  </v-table>
</template>
<style scoped>
  h1 {
    text-align: center;
  }
</style>