import React, { useState } from 'react';
import { StyleSheet, View, TextInput, Button, Alert } from 'react-native';
import { SelectList } from 'react-native-dropdown-select-list';

const SignUpScreen = ({ navigation }) => {



  
  const data = [
      {key:'1', value:'idoso',},
      {key:'2', value:'cuidador'},

  ]

  const [nome, setName] = useState('');
  const [email, setEmail] = useState('');
  const [senha, setPassword] = useState('');
  const [selected, setSelected] = React.useState("");


  const handleSignUp = async () => {
   
    const userData = {
      nome: nome,
      email: email,
      senha: senha,
      tipo: selected,
    };

    console.log(userData)

    const apiUrl = 'http://192.168.1.14:8084/users/register';
 

    await fetch(apiUrl, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(userData),
    
    })
      .then(response => response.json())
      .then(data => {
        console.log('Cadastro realizado:', data);
        navigation.navigate('Login');
        Alert.alert('Cadastro realizado com sucesso!');
      })
      .catch(error => {
        console.error('Erro ao cadastrar:', error);
        Alert.alert('Erro ao cadastrar. Por favor, tente novamente.');
      });
  };

  return (
    <View style={styles.container}>
      <TextInput
        placeholder="Nome"
        value={nome}
        onChangeText={text => setName(text)}
        style={styles.input}
        placeholderTextColor="#777"
      />
      <TextInput
        placeholder="Email"
        value={email}
        onChangeText={text => setEmail(text)}
        style={styles.input}
        placeholderTextColor="#777"
      /> 
        <View style={styles.dropdownContainer}>
        <SelectList
          setSelected={(val) => setSelected(val)} 
          data={data}
      
          save="value"
          placeholder="Selecione o tipo"
          title="Tipo de Usuário"
          titleStyle={styles.dropdownTitle}
          listItemTextStyle={styles.dropdownItemText}
          containerStyle={styles.dropdown}
          selectedItemStyle={styles.dropdownSelectedItem}
          dropdownImageStyle={styles.dropdownImage}
        />
         </View>
      <TextInput
        placeholder="Senha"
        value={senha}
        onChangeText={text => setPassword(text)}
        secureTextEntry
        style={styles.input}
        placeholderTextColor="#777"
      />
      <View style={styles.buttonContainer}>
        <Button title="Cadastrar" onPress={handleSignUp} color="#007bff" />
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    padding: 15,
    backgroundColor: '#fff',
  },
  input: {
    marginBottom: 20,
    backgroundColor: '#fff',
    paddingHorizontal: 10,
    paddingVertical: 8,
    borderWidth: 1,
    borderColor: '#8d8b8d',
    borderRadius: 8,
    fontSize: 16,
    color: '#333',
  },
  dropdownContainer: {
    marginBottom: 20,
    borderColor: '#ccc',
  },
  dropdownTitle: {
    color: '#333',
    fontSize: 16,
    paddingLeft: 10,
  },
  dropdownItemText: {
    color: '#333',
    fontSize: 16,
  },
  dropdown: {
    backgroundColor: '#f0f0f0',
    borderWidth: 1,
    borderColor: '#ccc',
    borderRadius: 5,
    paddingHorizontal: 10,
  },
  dropdownSelectedItem: {
    backgroundColor: '#007bff',
    color: '#fff',
  },
  dropdownImage: {
    tintColor: '#333',
  },
  buttonContainer: {
    marginTop: 20,
    shadowColor: '#000',
    shadowOffset: {
      width: 0,
      height: 2,
    },
    shadowOpacity: 0.25,
    shadowRadius: 3.84,
    elevation: 5,
    borderRadius: 5,
    overflow: 'hidden',
  },
});
export default SignUpScreen;
