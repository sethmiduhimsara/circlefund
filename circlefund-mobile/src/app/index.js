import { View, Text } from "react-native";

export default function LoginScreen() {
  return (
    <View
      style={{
        flex: 1,
        justifyContent: "center",
        alignItems: "center",
      }}
    >
      <Text style={{ fontSize: 28, fontWeight: "bold" }}>
        CircleFund
      </Text>

      <Text style={{ marginTop: 20 }}>
        Login Screen
      </Text>
    </View>
  );
}