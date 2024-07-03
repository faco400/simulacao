import React, { useState } from 'react';
import { StyleSheet, View, TextInput, Button } from 'react-native';
import { Alert } from 'react-native';
import axios from 'axios';
import AsyncStorage from '@react-native-async-storage/async-storage';

const LoginScreen = ({ navigation }) => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

 

  const handleLogin = async () => {
    
    try {
      const response = await axios.post('http://192.168.1.14:8081/token', {
        username: username,
        password: password
        
      }, { headers: {
        'Content-Type': 'multipart/form-data'
      },}
      );
      console.log('Response:', response);
     await AsyncStorage.setItem('jwtToken', response.data.access_token);
     await AsyncStorage.setItem('username', username);

     console.log('Token JWT:', response.data.access_token);

      Alert.alert('Login realizado com sucesso!');
      navigation.navigate('Home');
    } catch (error) {
      if (error.response) {
        console.log('Erro de resposta:', error.response.data);
        Alert.alert('Erro de resposta do servidor:', error.response.data.message);
      } else if (error.request) {
        console.log('Erro de requisição:', error.request);
        Alert.alert('Erro de rede. Verifique sua conexão e tente novamente.');
      } else {
        console.log('Erro desconhecido:', error.message);
        Alert.alert('Erro desconhecido:', error.message);
      }
    }
  };
  


  const goToSignUp = () => {
    navigation.navigate('Cadastro');
  };
  const goToLogin = () => {
    console.log('loguei teste ')
  };

  return (
    <View style={styles.container}>
      <TextInput
        placeholder="Email"
        style={styles.input}
        placeholderTextColor="#777"
        value={username}
        onChangeText={setUsername}
        
      />
      <TextInput
        placeholder="Senha"
        style={styles.input}
        secureTextEntry
        placeholderTextColor="#777"
        value={password}
        onChangeText={setPassword}
      />
      <Button title="Entrar" onPress={handleLogin} style={styles.button} />
      <View style={styles.signupContainer}>
        <Button
          title="Registrar"
          onPress={goToSignUp}
          style={[styles.button, styles.signupButton]}
        />
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
    marginBottom: 40,
    backgroundColor: '#f0f0f0', 
    paddingHorizontal: 10,
    paddingVertical: 8,
    borderWidth: 1,
    borderColor: '#ccc',
    borderRadius: 5,
    fontSize: 16,
    color: '#333',
  },
  button: {
    paddingVertical: 12,
    backgroundColor: '#007bff', 
    borderRadius: 5,
    marginBottom: 10, 
  },
  
  signupContainer: {
    marginTop: 30,
  },
  signupButton: {
    backgroundColor: '#28a745', 
  },
});

export default LoginScreen;
