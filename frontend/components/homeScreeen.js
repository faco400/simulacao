import React, { useState,useEffect } from 'react';
import { View, Text, StyleSheet } from 'react-native';
import AsyncStorage from '@react-native-async-storage/async-storage';

const HomeScreen = () => {
    const [token, setToken] = useState('');
    const [username, setUsername] = useState('');

    useEffect(() => {
      const fetchToken = async () => {
        const storedToken = await AsyncStorage.getItem('jwtToken');

        setToken(storedToken);
      };

      const fetchdData = async () => {
        const username = await AsyncStorage.getItem('username');
        
        setUsername(username);
      };
      fetchdData();
      fetchToken();
    }, []);


    return (
        <View style={styles.container}>
          <Text>Bem-vindo {username} </Text>
          <Text> </Text>
          <Text style={styles.token}>{token}</Text>
        </View>
      );
  
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  
});


export default HomeScreen;
